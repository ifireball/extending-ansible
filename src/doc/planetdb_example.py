#!/usr/bin/env python
# planetdb_example.py - Usage example for the 'planetdb' module
#
import planetdb

for planet in ['earth', 'dune', 'terra']:
    print(
        '%s canonical name is %s' % (
            planet,
            planetdb.lookup(planet)
        )
    )
