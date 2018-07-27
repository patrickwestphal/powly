from abc import abstractmethod, ABC

from exceptions import ClassCastException


class AsOWLClass(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @staticmethod
    def is_owl_class():
        return False

    def as_owl_class(self):
        if self.is_owl_class():
            return self
        else:
            raise ClassCastException('%s is not an OWLClass' % str(type(self)))
