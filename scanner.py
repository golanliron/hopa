#!/usr/bin/env python3
"""
Hopa - Voice Scanner (סורק קולות קוראים)
Scans calls for proposals from Israel and worldwide.

Usage:
    python scanner.py                    # Scan all sources
    python scanner.py --region israel    # Scan Israeli sources only
    python scanner.py --region intl      # Scan international sources only
    python scanner.py --category culture # Filter by category
    python scanner.py --output json      # Output format (json/csv/both)
"""

import argparse
import csv
import json
import logging
import os
import sys
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from scanners import IsraeliScanner, InternationalScanner, RSSScanner, APIScanner
from config import OUTPUT_DIR

console = Console()
logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def scan_all(region: str = "all") -> list[dict]:
    """Run all scanners and collect results."""
    results = []

    if region in ("all", "israel"):
        console.print("\n🔍 [bold blue]סורק מקורות ישראליים...[/bold blue]")
        israeli = IsraeliScanner()
        results.extend(c.to_dict() for c in israeli.scan())

    if region in ("all", "intl"):
        console.print("\n🌍 [bold green]Scanning international sources...[/bold green]")
        intl = InternationalScanner()
        results.extend(c.to_dict() for c in intl.scan())

        rss = RSSScanner()
        results.extend(c.to_dict() for c in rss.scan())

        api = APIScanner()
        results.extend(c.to_dict() for c in api.scan())

    return results


def filter_results(results: list[dict], category: str = None, topic: str = None) -> list[dict]:
    """Filter results by category and/or topic."""
    filtered = results
    if category:
        filtered = [r for r in filtered if r["category"] == category]
    if topic:
        topic_lower = topic.lower()
        filtered = [
            r for r in filtered
            if topic_lower in r.get("title", "").lower()
            or topic_lower in r.get("description", "").lower()
            or topic_lower in r.get("source", "").lower()
        ]
    return filtered


def display_results(results: list[dict]):
    """Display results in a formatted table."""
    if not results:
        console.print("\n[yellow]לא נמצאו קולות קוראים / No calls found.[/yellow]")
        return

    # Group by region
    israeli = [r for r in results if r["region"] == "israel"]
    international = [r for r in results if r["region"] == "international"]

    if israeli:
        console.print(
            Panel(
                f"[bold]נמצאו {len(israeli)} קולות קוראים מישראל[/bold]",
                style="blue",
            )
        )
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("כותרת / Title", style="white", max_width=50)
        table.add_column("תיאור / Description", style="dim white", max_width=40)
        table.add_column("מקור / Source", style="cyan", max_width=20)
        table.add_column("קטגוריה", style="green", max_width=12)
        table.add_column("מועד אחרון", style="red", max_width=18)

        for r in israeli:
            table.add_row(
                r["title"][:50],
                (r.get("description") or "")[:40],
                r["source"][:20],
                r["category"],
                r.get("deadline", "-") or "-",
            )
        console.print(table)

    if international:
        console.print(
            Panel(
                f"[bold]Found {len(international)} international calls[/bold]",
                style="green",
            )
        )
        table = Table(show_header=True, header_style="bold green")
        table.add_column("Title", style="white", max_width=50)
        table.add_column("Description", style="dim white", max_width=40)
        table.add_column("Source", style="cyan", max_width=20)
        table.add_column("Category", style="green", max_width=12)
        table.add_column("Deadline", style="red", max_width=18)
        table.add_column("Amount", style="yellow", max_width=15)

        for r in international:
            table.add_row(
                r["title"][:50],
                (r.get("description") or "")[:40],
                r["source"][:20],
                r["category"],
                r.get("deadline", "-") or "-",
                r.get("grant_amount", "-") or "-",
            )
        console.print(table)

    console.print(
        f"\n[bold]סה\"כ / Total: {len(results)} calls for proposals found[/bold]"
    )


def save_results(results: list[dict], output_format: str = "json"):
    """Save results to file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if output_format in ("json", "both"):
        filepath = os.path.join(OUTPUT_DIR, f"calls_{timestamp}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        console.print(f"\n💾 Saved JSON: [cyan]{filepath}[/cyan]")

    if output_format in ("csv", "both"):
        filepath = os.path.join(OUTPUT_DIR, f"calls_{timestamp}.csv")
        if results:
            with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
            console.print(f"💾 Saved CSV: [cyan]{filepath}[/cyan]")


def main():
    parser = argparse.ArgumentParser(
        description="Hopa - סורק קולות קוראים / Voice Scanner for Calls for Proposals"
    )
    parser.add_argument(
        "--region",
        choices=["all", "israel", "intl"],
        default="all",
        help="Region to scan (default: all)",
    )
    parser.add_argument(
        "--category",
        choices=[
            "innovation", "social", "culture", "film", "ngo", "government",
            "arts", "education", "research", "youth_at_risk", "social_mobility",
        ],
        help="Filter by category",
    )
    parser.add_argument(
        "--topic",
        help="Filter by topic keyword (e.g. 'נוער בסיכון', 'dropout prevention')",
    )
    parser.add_argument(
        "--output",
        choices=["json", "csv", "both"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save results to file",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose logging",
    )
    args = parser.parse_args()

    setup_logging(args.verbose)

    console.print(
        Panel(
            Text("🎯 Hopa - סורק קולות קוראים\nVoice Scanner for Calls for Proposals", justify="center"),
            style="bold magenta",
        )
    )

    results = scan_all(region=args.region)
    results = filter_results(results, category=args.category, topic=args.topic)
    display_results(results)

    if args.save:
        save_results(results, output_format=args.output)


if __name__ == "__main__":
    main()
