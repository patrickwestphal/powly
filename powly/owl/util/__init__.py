from itertools import chain

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


