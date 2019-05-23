# planetdb.py - Lookup plugin for using PlanetDB
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: planetdb
    author: Barak Korren (bkorren@redhat.com)
    version_added: "2.7"
    short_description: Lookup planet name in the Planets DB
    description:
        - This plugin looks up the given names in the Planets DB and returns
          the canonical names for those planes for use with an Ansible device
    options:
        _terms:
            description: names of planets to look up
            required: True
"""
import planetdb

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        try:
            return [planetdb.lookup(term) for term in terms]
        except planetdb.PlanetdbLookupError:
            raise AnsibleError('Failed to lookup destination planet')
