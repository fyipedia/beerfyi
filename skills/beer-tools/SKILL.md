---
name: beer-tools
description: Search 113 beer styles, 82 hops, 41 malts, and 29 yeasts with BJCP classification and brewing science data.
---

# Beer Tools

Beer style search and brewing reference powered by [beerfyi](https://beerfyi.com/) -- a comprehensive beer knowledge platform covering 113 styles, 82 hops, 41 malts, and 29 yeasts.

## Setup

Install the MCP server:

```bash
pip install "beerfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "beerfyi": {
            "command": "python",
            "args": ["-m", "beerfyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `beer_search` | Search beer styles, hops, malts, yeasts, and brewing terms by keyword |

## When to Use

- Looking up beer styles and their BJCP classification
- Researching hop varieties (alpha acids, flavor profiles, origins)
- Finding malt characteristics for recipe formulation
- Exploring yeast strains and fermentation profiles
- Learning about brewing techniques and terminology

## Links

- [113 Beer Styles](https://beerfyi.com/styles/)
- [82 Hop Varieties](https://beerfyi.com/hops/)
- [Brewing Glossary](https://beerfyi.com/glossary/)
- [API Documentation](https://beerfyi.com/developers/)
- [PyPI Package](https://pypi.org/project/beerfyi/)
