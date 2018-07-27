from abc import abstractmethod, ABC

from exceptions import ClassCastException


class AsOWLAnnotationProperty(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @staticmethod
    def is_owl_annotation_property():
        return False

    def as_owl_annotation_property(self):
        if self.is_owl_annotation_property():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLAnnotationProperty' % str(type(self)))
