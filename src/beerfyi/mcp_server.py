"""MCP server for beerfyi — beer knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install beerfyi[mcp]``

Run as a standalone server::

    python -m beerfyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "beerfyi": {
                "command": "python",
                "args": ["-m", "beerfyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("beerfyi")


@mcp.tool()
def beer_search(query: str) -> str:
    """Search beer styles, ingredients, and brewing terms from BeerFYI.

    Search the BeerFYI encyclopedia for beer styles (IPA, Stout, Lager, etc.),
    ingredients (hops, malts, yeasts), brewing terms, breweries, and more.

    Args:
        query: Search term (e.g. "ipa", "cascade hops", "belgian", "stout").
    """
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        results = api.search(query)

    items = results.get("results", [])
    if not items:
        return f"No results found for '{query}'."

    lines = [
        f"## Beer Search: {query}",
        "",
        f"Found {len(items)} result(s):",
        "",
        "| Type | Name | URL |",
        "|------|------|-----|",
    ]
    for item in items:
        item_type = item.get("type", "")
        name = item.get("name", "")
        url = item.get("url", "")
        lines.append(f"| {item_type} | {name} | {url} |")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
