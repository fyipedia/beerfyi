"""MCP server for beerfyi — AI assistant tools for beerfyi.com.

Run: uvx --from "beerfyi[mcp]" python -m beerfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BeerFYI")


@mcp.tool()
def list_hops(limit: int = 20, offset: int = 0) -> str:
    """List hops from beerfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        data = api.list_hops(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No hops found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_hop(slug: str) -> str:
    """Get detailed information about a specific hop.

    Args:
        slug: URL slug identifier for the hop.
    """
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        data = api.get_hop(slug)
        return str(data)


@mcp.tool()
def list_malts(limit: int = 20, offset: int = 0) -> str:
    """List malts from beerfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        data = api.list_malts(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No malts found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_beer(query: str) -> str:
    """Search beerfyi.com for beer styles, hops, malts, and breweries.

    Args:
        query: Search query string.
    """
    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
