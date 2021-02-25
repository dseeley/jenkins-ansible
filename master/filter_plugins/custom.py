#!/usr/bin/env python

from distutils.version import LooseVersion

def semver_sort(value):
    return sorted(value, key=LooseVersion)


class FilterModule(object):
    semver_sort = {
        'semver_sort': semver_sort,
    }

    def filters(self):
        return self.semver_sort
