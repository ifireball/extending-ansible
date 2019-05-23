# planetdb/__init__.py - Planet name lookup database module
#
PLANET_NAME_MAP = {
    'terra': 'earth',
    'dune': 'arrakis',
}


class PlanetdbLookupError(Exception):
    """Excpetion raised when looked up planed is not found in the Planets DB
    """


def lookup(name):
    """Lookup up a planet name in the Planets database

    :param str name: The name to lookup in the database

    :rtype: str
    :returns: The canonical name for the given planet. Raises
              PlanetdbLookupError if not found
    """
    return PLANET_NAME_MAP.get(name.lower(), name).capitalize()
