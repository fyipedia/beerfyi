"""Command-line interface for beerfyi.

Requires the ``cli`` extra: ``pip install beerfyi[cli]``

Usage::

    beerfyi search "ipa"              # Search beer styles, ingredients, terms
    beerfyi search "hops"             # Search for hops
    beerfyi search "belgian"          # Search for Belgian styles
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="beerfyi",
    help="Beer knowledge API client — search beer styles, ingredients, and brewing terms.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'ipa', 'hops', 'lager')"),
) -> None:
    """Search beer styles, ingredients, and brewing terms from BeerFYI."""
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        results = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name", style="bold")
    table.add_column("URL")

    items = results.get("results", [])
    if not items:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    for item in items:
        table.add_row(
            item.get("type", ""),
            item.get("name", ""),
            item.get("url", ""),
        )
    console.print(table)


if __name__ == "__main__":
    app()
