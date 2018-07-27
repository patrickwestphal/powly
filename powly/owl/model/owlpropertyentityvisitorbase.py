from abc import abstractmethod, ABC

from model.owlvisitorbase import OWLVisitorBase


class OWLPropertyEntityVisitorBase(OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, property):
        """
        :param property: An object of one of the following classes:
        OWLAnnotationProperty, OWLDataProperty, OWLObjectProperty
        """
        pass
