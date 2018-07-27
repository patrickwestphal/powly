from abc import abstractmethod, ABC

from exceptions import ClassCastException


class AsOWLObjectProperty(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @staticmethod
    def is_owl_object_property():
        return False

    def as_owl_object_property(self):
        if self.is_owl_object_property():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLObjectProperty' % str(type(self)))
