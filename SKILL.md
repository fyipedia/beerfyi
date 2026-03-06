---
name: beer-tools
description: Search 112 beer styles, 82 hop varieties, 41 malts, 29 yeast strains, and brewing terminology from BeerFYI. Use when answering questions about beer styles, BJCP guidelines, hops, malts, or brewing science.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://beerfyi.com/"
---

# BeerFYI -- Beer Tools for AI Agents

Beer knowledge API client for Python. Search 112 beer styles, 82 hop varieties, 41 malts, 29 yeast strains, and brewing terminology from BeerFYI -- the complete beer style reference following BJCP guidelines with 150 expert guides.

**Install**: `pip install beerfyi[api]` -- **Web**: [beerfyi.com](https://beerfyi.com/) -- **API**: [REST API](https://beerfyi.com/developers/) -- **PyPI**: [beerfyi](https://pypi.org/project/beerfyi/)

## When to Use

- User asks about beer styles, BJCP guidelines, or style parameters (IBU, SRM, ABV)
- User needs hop variety profiles (alpha acid, aroma, usage)
- User wants malt or yeast strain information
- User asks about brewing techniques or terminology
- User needs to compare beer styles

## Tools

### `BeerFYI` API Client

HTTP client for the beerfyi.com REST API. Requires `pip install beerfyi[api]`.

```python
from beerfyi.api import BeerFYI

with BeerFYI() as api:
    results = api.search("ipa")        # Search styles, hops, malts, yeast, glossary
```

**Methods:**
- `search(query: str) -> dict` -- Search beer styles, ingredients, and brewing terms

## REST API (No Auth Required)

```bash
# Search
curl "https://beerfyi.com/api/v1/search/?q=ipa"

# Beer style detail
curl "https://beerfyi.com/api/v1/styles/new-england-ipa/"

# Hop variety detail
curl "https://beerfyi.com/api/v1/hops/citra/"

# Glossary term
curl "https://beerfyi.com/api/v1/glossary/ibu/"

# Compare two styles
curl "https://beerfyi.com/api/v1/compare/west-coast-ipa/new-england-ipa/"
```

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
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two beer styles |
| GET | `/api/v1/random/` | Random beer style |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://beerfyi.com/api/v1/openapi.json)

## Beer Style Categories

| Category | Description | Notable Styles |
|----------|-------------|----------------|
| Ale | Top-fermented, warm fermentation (15-24C) | Pale Ale, IPA, Stout, Porter, Belgian Tripel |
| Lager | Bottom-fermented, cold conditioning (7-13C) | Pilsner, Helles, Bock, Dunkel, Marzen |
| Wheat | Significant wheat malt proportion (30-70%) | Hefeweizen, Witbier, Berliner Weisse |
| Stout | Roasted barley, dark color, rich body | Dry Stout, Imperial Stout, Milk Stout |
| IPA | Hop-forward, American craft innovation | West Coast IPA, New England IPA, Double IPA |
| Sour | Intentional acidity from wild yeast/bacteria | Lambic, Gose, Flanders Red, Kettle Sour |
| Belgian | Complex yeast character, phenols, esters | Dubbel, Tripel, Quadrupel, Saison |

## Key Brewing Metrics

| Metric | Abbreviation | Description |
|--------|-------------|-------------|
| International Bitterness Units | IBU | Hop bitterness (0-120+) |
| Standard Reference Method | SRM | Beer color (1=pale straw, 40+=black) |
| Original Gravity | OG | Sugar content before fermentation |
| Final Gravity | FG | Residual sugar after fermentation |
| Attenuation | % | Sugar converted to alcohol |

## Demo

![BeerFYI demo](https://raw.githubusercontent.com/fyipedia/beerfyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
