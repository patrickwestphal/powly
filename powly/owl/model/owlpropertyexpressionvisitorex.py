from abc import abstractmethod, ABC

from powly.owl.model.owlpropertyentityvisitorexbase import OWLPropertyEntityVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLPropertyExpressionVisitorEx(
        OWLPropertyEntityVisitorExBase, OWLVisitorExBase, ABC):

    @abstractmethod
    def visit(self, property):
        """
        :param property: An object of one of the following classes:
        OWLObjectInverseOf; or one of these classes: OWLAnnotationProperty,
        OWLDataProperty, OWLObjectProperty
        """
        pass
