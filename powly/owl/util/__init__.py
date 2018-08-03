from itertools import chain, zip_longest

import itertools

from collections import Iterable

from powly.owl.model.hascomponent import HasComponents


def flat_components(root):
    """
    :param root: A HasComponents object
    :return: A generator iterating through all nested components
    """
    yield root

    for c in filter(lambda e: e != root, root.components()):
        for sc in _flat_iteration(c):
            yield sc


def _flat_iteration(component):
    if isinstance(component, HasComponents):
        return [component] + \
            chain(
                (_flat_iteration(subcomp)
                 for subcomp in component.components()))
    else:
        return [component]


def compare_iterators(set1, set2):
    """
    :return: negative value if set1 comes before set2, positive value if set2
    comes before set1, 0 if the two sets are equal or incomparable.
    """
    for e1, e2 in zip_longest(set1, set2):
        if e1 is None:
            return -1
        elif e2 is None:
            return 1

        if isinstance(e1, str) and isinstance(e2, str):
            if e1 < e2:
                return -1
            elif e1 > e2:
                return 1
            else:
                return 0

        if isinstance(e1, Iterable) and isinstance(e2, Iterable):
            print('Took firsts if')
            diff = compare_iterators(e1, e2)

        elif hasattr(e1, 'compare_to') and hasattr(e2, 'compare_to'):
            print('Took second if')
            diff = e1.compare_to(e2)

        else:
            raise RuntimeError(
                'Incomparable types: %s with class %s, %s with class %s found '
                'while comparing iterators' % (str(e1), str(type(e1)), str(e2),
                                               str(type(e2))))

        if diff != 0:
            return diff
