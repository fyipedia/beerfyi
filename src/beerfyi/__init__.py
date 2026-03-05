"""beerfyi — Beer knowledge API client for developers.

Search beer styles, ingredients, and brewing terminology from BeerFYI.

Usage::

    from beerfyi.api import BeerFYI

    with BeerFYI() as api:
        results = api.search("ipa")
        print(results)
"""

__version__ = "0.1.0"
