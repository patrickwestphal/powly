from abc import abstractmethod, ABC

from exceptions import ClassCastException


class AsOWLDataProperty(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @staticmethod
    def is_owl_data_property():
        return False

    def as_owl_data_property(self):
        if self.is_owl_data_property():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLDataProperty' % str(type(self)))
