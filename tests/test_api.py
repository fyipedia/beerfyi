"""Tests for beerfyi.api — API client initialization and URL construction."""

from beerfyi.api import BeerFYI


class TestBeerFYIInit:
    def test_default_base_url(self) -> None:
        client = BeerFYI()
        assert str(client._client.base_url) == "https://beerfyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = BeerFYI(base_url="https://test.beerfyi.com")
        assert str(client._client.base_url) == "https://test.beerfyi.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = BeerFYI()
        assert client._client.timeout.connect == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = BeerFYI(timeout=30.0)
        assert client._client.timeout.connect == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with BeerFYI() as api:
            assert str(api._client.base_url) == "https://beerfyi.com"


class TestBeerFYIVersion:
    def test_version(self) -> None:
        from beerfyi import __version__

        assert __version__ == "0.1.0"

    def test_version_is_string(self) -> None:
        from beerfyi import __version__

        assert isinstance(__version__, str)
