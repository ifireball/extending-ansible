#!/usr/bin/env python
# planetdb_example.py - Usage example for the 'planetdb' module
#
from planetdb import lookup

for planet in ['earth', 'dune', 'terra']:
    print('{} canonical name is {}'.format(
        planet, lookup(planet)
    ))
