# beerfyi

[![PyPI](https://img.shields.io/pypi/v/beerfyi)](https://pypi.org/project/beerfyi/)
[![Python](https://img.shields.io/pypi/pyversions/beerfyi)](https://pypi.org/project/beerfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Beer knowledge API client for Python. Search 112 beer styles, 82 hop varieties, 41 malts, 29 yeast strains, and brewing terminology from [BeerFYI](https://beerfyi.com) -- the complete beer style reference with 150 expert guides covering BJCP classifications, ingredient science, and brewing techniques.

> **Explore beer at [beerfyi.com](https://beerfyi.com)** -- [Beer Styles](https://beerfyi.com/styles/) | [Hops](https://beerfyi.com/hops/) | [Malts](https://beerfyi.com/malts/) | [Yeast](https://beerfyi.com/yeast/) | [Brewing Guides](https://beerfyi.com/guides/)

<p align="center">
  <img src="demo.gif" alt="beerfyi demo -- beer style API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on BeerFYI](#what-youll-find-on-beerfyi)
  - [Beer Style Categories](#beer-style-categories)
  - [Hop Varieties](#hop-varieties)
  - [Malts and Grains](#malts-and-grains)
  - [Yeast Strains](#yeast-strains)
  - [Key Brewing Metrics](#key-brewing-metrics)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Beer](#learn-more-about-beer)
- [Beverage FYI Family](#beverage-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install beerfyi[api]     # API client (httpx)
pip install beerfyi[cli]     # + CLI (typer, rich)
pip install beerfyi[mcp]     # + MCP server
pip install beerfyi[all]     # Everything
```

## Quick Start

```python
from beerfyi.api import BeerFYI

with BeerFYI() as api:
    # Search beer styles, hops, malts, yeast, glossary terms
    results = api.search("ipa")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("ibu")
    print(term["definition"])
```

## What You'll Find on BeerFYI

BeerFYI is a comprehensive beer reference covering 112 beer styles, 82 hop varieties, 41 malts, 29 yeast strains, and 150 expert guides. The database follows the Beer Judge Certification Program (BJCP) style guidelines -- the global standard for beer style classification used in homebrewing competitions and professional brewing.

### Beer Style Categories

Beer styles are organized into broad families based on fermentation method, yeast type, and regional brewing traditions. Each style has defined parameters for appearance, aroma, flavor, and mouthfeel:

| Category | Description | Notable Styles |
|----------|-------------|----------------|
| Ale | Top-fermented, warm fermentation (15-24C) | Pale Ale, IPA, Stout, Porter, Belgian Tripel |
| Lager | Bottom-fermented, cold conditioning (7-13C) | Pilsner, Helles, Bock, Dunkel, Marzen |
| Wheat | Significant wheat malt proportion (30-70%) | Hefeweizen, Witbier, Berliner Weisse |
| Stout | Roasted barley, dark color, rich body | Dry Stout, Imperial Stout, Milk Stout, Oatmeal Stout |
| IPA | Hop-forward, American craft innovation | West Coast IPA, New England IPA, Double IPA, Session IPA |
| Sour | Intentional acidity from wild yeast/bacteria | Lambic, Gose, Flanders Red, Kettle Sour |
| Belgian | Complex yeast character, phenols, esters | Dubbel, Tripel, Quadrupel, Saison, Witbier |
| Wild/Spontaneous | Open-air inoculation, Brettanomyces | Lambic, Gueuze, American Wild Ale |

### Hop Varieties

BeerFYI catalogs 82 hop varieties with detailed profiles including alpha acid percentage, aroma descriptors, typical usage (bittering, flavor, aroma, dry-hop), and recommended beer styles. Hops provide bitterness to balance malt sweetness, contribute floral, citrus, pine, or tropical aromas, and act as a natural preservative.

Major hop-growing regions include the Pacific Northwest (Yakima Valley), Germany (Hallertau, Tettnang), England (Kent), Czech Republic (Saaz), and New Zealand (Nelson). Each region's terroir influences hop character -- Cascade from Yakima delivers different citrus notes than Cascade grown in other regions.

### Malts and Grains

The 41 malts in the database cover base malts (Pale, Pilsner, Munich, Vienna), specialty malts (Crystal, Caramel, Chocolate, Black Patent), and adjuncts (wheat, oats, rye, corn, rice). Malt provides fermentable sugars, body, color (measured in SRM/Lovibond), and flavor complexity.

The malting process -- steeping, germination, and kilning -- transforms raw barley into brewing malt. Temperature and duration of kilning determine color and flavor: light kilning produces pale malt (2-4 SRM), moderate kilning creates Munich malt (8-10 SRM), and high-temperature roasting yields chocolate malt (350-450 SRM).

### Yeast Strains

BeerFYI tracks 29 yeast strains with fermentation temperature ranges, attenuation percentages, flocculation characteristics, and flavor contributions. Yeast is the most influential ingredient in beer -- the same wort fermented with different yeast strains produces fundamentally different beers.

Major yeast categories include clean ale strains (American, English), expressive Belgian strains (Abbey, Saison), clean lager strains (Bohemian, Bavarian), and wild cultures (Brettanomyces, Lactobacillus, Pediococcus).

### Key Brewing Metrics

| Metric | Abbreviation | Description |
|--------|-------------|-------------|
| International Bitterness Units | IBU | Measures hop bitterness (0-120+) |
| Standard Reference Method | SRM | Measures beer color (1=pale straw, 40+=black) |
| Alcohol By Volume | ABV | Alcohol content percentage |
| Original Gravity | OG | Sugar content before fermentation |
| Final Gravity | FG | Residual sugar after fermentation |
| Attenuation | % | Percentage of sugar converted to alcohol |

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/styles/` | List all 112 beer styles |
| GET | `/api/v1/styles/{slug}/` | Beer style detail with BJCP parameters |
| GET | `/api/v1/hops/` | List all 82 hop varieties |
| GET | `/api/v1/hops/{slug}/` | Hop variety detail with alpha acids |
| GET | `/api/v1/malts/` | List all 41 malts |
| GET | `/api/v1/malts/{slug}/` | Malt detail with color, flavor |
| GET | `/api/v1/yeast/` | List all 29 yeast strains |
| GET | `/api/v1/yeast/{slug}/` | Yeast strain detail |
| GET | `/api/v1/glossary/` | List all brewing terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two beer styles |
| GET | `/api/v1/random/` | Random beer style |
| GET | `/api/v1/guides/` | List all 150 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://beerfyi.com/api/v1/styles/new-england-ipa/"
```

```json
{
  "slug": "new-england-ipa",
  "name": "New England IPA",
  "category": "IPA",
  "description": "A hazy, juicy, hop-forward ale emphasizing tropical fruit and citrus aromas with soft bitterness and a creamy mouthfeel.",
  "abv_min": 6.0,
  "abv_max": 9.0,
  "ibu_min": 25,
  "ibu_max": 60,
  "srm_min": 3,
  "srm_max": 7,
  "og_min": 1.060,
  "og_max": 1.085,
  "recommended_hops": ["Citra", "Mosaic", "Galaxy", "El Dorado"],
  "url": "https://beerfyi.com/styles/new-england-ipa/"
}
```

Full API documentation: [beerfyi.com/developers/](https://beerfyi.com/developers/).
OpenAPI 3.1.0 spec: [beerfyi.com/api/v1/openapi.json](https://beerfyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search beer styles, hops, malts, yeast
beerfyi search "ipa"
beerfyi search "cascade hops"
beerfyi search "belgian"

# Look up brewing terms
beerfyi term "ibu"
beerfyi term "attenuation"

# Search by ingredient
beerfyi search "citra"
beerfyi search "crystal malt"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted beer queries:

```bash
python -m beerfyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "beerfyi": {
      "command": "uvx",
      "args": ["--from", "beerfyi[mcp]", "python", "-m", "beerfyi.mcp_server"]
    }
  }
}
```

**Tools**: `beer_search`, `beer_glossary_term`

## API Client

```python
from beerfyi.api import BeerFYI

with BeerFYI() as api:
    # Search across styles, hops, malts, yeast, glossary
    results = api.search("stout")

    # Look up brewing terminology
    term = api.glossary_term("dry-hopping")
    print(term["definition"])

    # Compare two beer styles
    comparison = api.compare("west-coast-ipa", "new-england-ipa")

    # Get a random beer style
    random_style = api.random()
```

## Learn More About Beer

- **Reference**: [Beer Styles](https://beerfyi.com/styles/) | [Hops](https://beerfyi.com/hops/) | [Malts](https://beerfyi.com/malts/) | [Yeast](https://beerfyi.com/yeast/)
- **Glossary**: [Brewing Terminology](https://beerfyi.com/glossary/)
- **Guides**: [Brewing Guides](https://beerfyi.com/guides/)
- **Compare**: [Style Comparisons](https://beerfyi.com/compare/)
- **API**: [Developer Docs](https://beerfyi.com/developers/) | [OpenAPI Spec](https://beerfyi.com/api/v1/openapi.json)

## Beverage FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktail recipes, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| **BeerFYI** | [beerfyi.com](https://beerfyi.com) | **112 beer styles, hops, malts, yeast, brewing guides** |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis -- [emojifyi.com](https://emojifyi.com) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com) |
| vinofyi | [PyPI](https://pypi.org/project/vinofyi/) | -- | Wine API client -- grapes, regions, wineries -- [vinofyi.com](https://vinofyi.com) |
| **beerfyi** | [PyPI](https://pypi.org/project/beerfyi/) | -- | **Beer styles, hops, malts API -- [beerfyi.com](https://beerfyi.com)** |
| brewfyi | [PyPI](https://pypi.org/project/brewfyi/) | -- | Coffee varieties, brew methods API -- [brewfyi.com](https://brewfyi.com) |
| whiskeyfyi | [PyPI](https://pypi.org/project/whiskeyfyi/) | -- | Whiskey expressions, distilleries API -- [whiskeyfyi.com](https://whiskeyfyi.com) |
| teafyi | [PyPI](https://pypi.org/project/teafyi/) | -- | Tea varieties, teaware API -- [teafyi.com](https://teafyi.com) |
| nihonshufyi | [PyPI](https://pypi.org/project/nihonshufyi/) | -- | Sake grades, breweries API -- [nihonshufyi.com](https://nihonshufyi.com) |
| drinkfyi | [PyPI](https://pypi.org/project/drinkfyi/) | -- | Unified beverage hub -- 7 sites -- [fyipedia.com](https://fyipedia.com) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI: `fyi color info FF6B35` -- [fyipedia.com](https://fyipedia.com) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP hub for AI assistants -- [fyipedia.com](https://fyipedia.com) |

## License

MIT
