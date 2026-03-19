#!/usr/bin/env python3
"""
Hopa - Daily Scanner Scheduler (תזמון סריקה יומית)
Runs the voice scanner automatically once per day.

Usage:
    python scheduler.py                  # Start daily scheduler
    python scheduler.py --time 09:00     # Set custom scan time
    python scheduler.py --now            # Run immediately + schedule daily
"""

import argparse
import logging
import time
import signal
import sys
from datetime import datetime

import schedule
from rich.console import Console
from rich.panel import Panel

from scanner import scan_all, display_results, save_results
from config import SCAN_TIME

console = Console()
logger = logging.getLogger(__name__)
running = True


def signal_handler(sig, frame):
    global running
    console.print("\n[yellow]Stopping scheduler...[/yellow]")
    running = False


def daily_scan():
    """Run a full scan and save results."""
    console.print(
        Panel(
            f"[bold]🔄 Starting daily scan - {datetime.now().strftime('%Y-%m-%d %H:%M')}[/bold]",
            style="magenta",
        )
    )

    try:
        results = scan_all(region="all")
        display_results(results)
        save_results(results, output_format="both")

        console.print(
            f"\n[green]✅ Daily scan complete: {len(results)} calls found[/green]"
        )
    except Exception as e:
        logger.error("Daily scan failed: %s", e)
        console.print(f"\n[red]❌ Scan failed: {e}[/red]")


def main():
    parser = argparse.ArgumentParser(
        description="Hopa - Daily Scanner Scheduler (תזמון סריקה יומית)"
    )
    parser.add_argument(
        "--time",
        default=SCAN_TIME,
        help=f"Daily scan time in HH:MM format (default: {SCAN_TIME})",
    )
    parser.add_argument(
        "--now",
        action="store_true",
        help="Run scan immediately before starting scheduler",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose logging",
    )
    args = parser.parse_args()

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    console.print(
        Panel(
            f"[bold]📅 Hopa Daily Scheduler[/bold]\n"
            f"Scanning every day at {args.time}\n"
            f"Press Ctrl+C to stop",
            style="blue",
        )
    )

    if args.now:
        daily_scan()

    schedule.every().day.at(args.time).do(daily_scan)
    console.print(f"[dim]Next scan scheduled at: {args.time}[/dim]\n")

    while running:
        schedule.run_pending()
        time.sleep(60)

    console.print("[yellow]Scheduler stopped.[/yellow]")


if __name__ == "__main__":
    main()
