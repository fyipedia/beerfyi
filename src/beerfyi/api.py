"""HTTP API client for beerfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install beerfyi[api]``

Usage::

    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        results = api.search("ipa")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class BeerFYI:
    """API client for the beerfyi.com REST API.

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

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def search(self, query: str) -> dict[str, Any]:
        """Search beer styles, ingredients, and brewing terms.

        Args:
            query: Search term (e.g. ``"ipa"``, ``"hops"``, ``"lager"``).
        """
        return self._get("/api/search/", q=query)

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> BeerFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
