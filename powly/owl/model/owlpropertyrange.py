from abc import abstractmethod, ABC

from model.owlobject import OWLObject


class OWLPropertyRange(OWLObject, ABC):
    """
    A marker interface, for objects that can be the ranges of properties.
    """
    @abstractmethod
    def __init__(self, *args):
        pass
