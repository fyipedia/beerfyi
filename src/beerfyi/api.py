"""HTTP API client for beerfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install beerfyi[api]``

Usage::

    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        items = api.list_breweries()
        detail = api.get_brewery("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class BeerFYI:
    """API client for the beerfyi.com REST API.

    Provides typed access to all beerfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://beerfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://beerfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_breweries(self, **params: Any) -> dict[str, Any]:
        """List all breweries."""
        return self._get("/api/v1/breweries/", **params)

    def get_brewery(self, slug: str) -> dict[str, Any]:
        """Get brewery by slug."""
        return self._get(f"/api/v1/breweries/" + slug + "/")

    def list_categories(self, **params: Any) -> dict[str, Any]:
        """List all categories."""
        return self._get("/api/v1/categories/", **params)

    def get_category(self, slug: str) -> dict[str, Any]:
        """Get category by slug."""
        return self._get(f"/api/v1/categories/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_hops(self, **params: Any) -> dict[str, Any]:
        """List all hops."""
        return self._get("/api/v1/hops/", **params)

    def get_hop(self, slug: str) -> dict[str, Any]:
        """Get hop by slug."""
        return self._get(f"/api/v1/hops/" + slug + "/")

    def list_malts(self, **params: Any) -> dict[str, Any]:
        """List all malts."""
        return self._get("/api/v1/malts/", **params)

    def get_malt(self, slug: str) -> dict[str, Any]:
        """Get malt by slug."""
        return self._get(f"/api/v1/malts/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_styles(self, **params: Any) -> dict[str, Any]:
        """List all styles."""
        return self._get("/api/v1/styles/", **params)

    def get_style(self, slug: str) -> dict[str, Any]:
        """Get style by slug."""
        return self._get(f"/api/v1/styles/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_yeasts(self, **params: Any) -> dict[str, Any]:
        """List all yeasts."""
        return self._get("/api/v1/yeasts/", **params)

    def get_yeast(self, slug: str) -> dict[str, Any]:
        """Get yeast by slug."""
        return self._get(f"/api/v1/yeasts/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> BeerFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
