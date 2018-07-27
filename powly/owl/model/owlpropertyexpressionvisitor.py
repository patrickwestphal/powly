from abc import abstractmethod, ABC

from model.owlpropertyentityvisitorbase import OWLPropertyEntityVisitorBase
from model.owlvisitorbase import OWLVisitorBase


class OWLPropertyExpressionVisitor(
        OWLPropertyEntityVisitorBase, OWLVisitorBase, ABC):
    """
    An interface to object that can visit the different types of property
    expressions.
    """
    @abstractmethod
    def visit(self, property):
        """
        :param property: An object of one of the following classes:
        OWLObjectInverseOf; or one of these classes: OWLAnnotationProperty,
        OWLDataProperty, OWLObjectProperty
        """
        pass
