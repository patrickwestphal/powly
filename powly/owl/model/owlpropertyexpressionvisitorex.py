from abc import abstractmethod, ABC

from model.owlpropertyentityvisitorexbase import OWLPropertyEntityVisitorExBase
from model.owlvisitorexbase import OWLVisitorExBase


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
