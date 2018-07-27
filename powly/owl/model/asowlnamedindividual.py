from abc import abstractmethod, ABC

from powly.owl.exceptions import ClassCastException


class AsOWLNamedIndividual(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @staticmethod
    def is_owl_named_individual():
        return False

    def as_owl_named_individual(self):
        if self.is_owl_named_individual():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLNamedIndividual' % str(type(self)))
