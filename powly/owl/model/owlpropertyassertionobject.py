from abc import ABC

from powly.owl.model.owlobject import OWLObject


class OWLPropertyAssertionObject(OWLObject, ABC):
    """
    A marker interface for the types of property assertion objects
    (individuals and literals) that are the objects of property assertions.
    """
