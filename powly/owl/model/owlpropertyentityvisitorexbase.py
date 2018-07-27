from abc import abstractmethod, ABC

from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLPropertyEntityVisitorExBase(OWLVisitorExBase, ABC):
    @abstractmethod
    def visit(self, property):
        """
        :param property: An object of one of the following classes:
        OWLAnnotationProperty, OWLDataProperty, OWLObjectProperty
        """
        pass
