# beerfyi

Beer knowledge API client for developers — search beer styles, ingredients, and brewing terms from BeerFYI.

## Install

```bash
pip install beerfyi          # Core (zero deps)
pip install beerfyi[cli]     # + CLI (typer, rich)
pip install beerfyi[mcp]     # + MCP server
pip install beerfyi[api]     # + API client (httpx)
pip install beerfyi[all]     # Everything
```

## Quick Start

```python
from beerfyi.api import BeerFYI

with BeerFYI() as api:
    results = api.search("ipa")
    print(results)
```

## CLI

```bash
beerfyi search "ipa"
beerfyi search "cascade hops"
beerfyi search "belgian"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m beerfyi.mcp_server
```

Tools: `beer_search`

## API Client

```python
from beerfyi.api import BeerFYI

with BeerFYI() as api:
    # Search beer styles, ingredients, and brewing terms
    results = api.search("stout")
```

## Links

- [BeerFYI](https://beerfyi.com) — Beer encyclopedia with styles, ingredients, and brewing guides
- [PyPI](https://pypi.org/project/beerfyi/)
- [GitHub](https://github.com/fyipedia/beerfyi)
- [FYIPedia](https://fyipedia.com) — Open-source developer tools ecosystem
