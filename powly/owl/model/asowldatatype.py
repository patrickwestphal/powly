from abc import abstractmethod, ABC

from exceptions import ClassCastException


class AsOWLDatatype(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    def is_owl_datatype(self):
        return False

    def as_owl_datatype(self):
        if self.is_owl_datatype():
            return self
        else:
            raise ClassCastException(
                '% is not an OWLDatatype' % str(type(self)))
