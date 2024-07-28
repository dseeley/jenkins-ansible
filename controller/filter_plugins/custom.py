#!/usr/bin/env python

import functools

def semantic_sort(version_list):
    def parse_version(version):
        # Split the version into parts
        parts = version.split('.')
        parsed_parts = []
        for part in parts:
            # Separate numeric and non-numeric parts
            num_part = ''
            suffix = ''
            for char in part:
                if char.isdigit():
                    num_part += char
                else:
                    suffix += char
            # Convert numeric part to an integer and keep suffix as is
            num_part = int(num_part) if num_part else 0
            parsed_parts.append((num_part, suffix))
        return parsed_parts

    def compare_versions(v1, v2):
        # Compare each part of the versions
        for p1, p2 in zip(v1, v2):
            if p1[0] != p2[0]:  # Compare numeric parts
                return p1[0] - p2[0]
            if p1[1] != p2[1]:  # Compare suffix parts lexically
                return -1 if p1[1] < p2[1] else 1
        # If one version is a prefix of the other
        return len(v1) - len(v2)

    # Parse all versions
    parsed_versions = [(parse_version(v), v) for v in version_list]
    # Sort based on parsed version
    parsed_versions.sort(key=functools.cmp_to_key(lambda x, y: compare_versions(x[0], y[0])))

    # Return the sorted original versions
    return [v[1] for v in parsed_versions]



class FilterModule(object):
    semver_sort = {
        'semver_sort': semantic_sort,
    }

    def filters(self):
        return self.semver_sort
