#!/usr/bin/env python

from pkg_resources import parse_version

def semver_sort(value):
    return sorted(value, key=parse_version)


class FilterModule(object):
    semver_sort = {
        'semver_sort': semver_sort,
    }

    def filters(self):
        return self.semver_sort
