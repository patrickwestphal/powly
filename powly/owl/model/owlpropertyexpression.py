from abc import abstractmethod, ABC

from powly.owl.exceptions import ClassCastException
from powly.owl.model.asowldataproperty import AsOWLDataProperty
from powly.owl.model.asowlobjectproperty import AsOWLObjectProperty
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlpropertyexpressionvisitor import \
    OWLPropertyExpressionVisitor
from powly.owl.model.owlpropertyexpressionvisitorex import \
    OWLPropertyExpressionVisitorEx


class OWLPropertyExpression(
    OWLObject, AsOWLObjectProperty, AsOWLDataProperty, ABC):
    """
    Represents a property or possibly the inverse of a property.
    """

    @abstractmethod
    def __init__(self, *args):
        pass

    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLPropertyExpressionVisitor, OWLPropertyExpressionVisitorEx; or one of
        these classes: OWLObjectVisitor, OWLObjectVisitorEx
        :return:
        """
        if isinstance(visitor, OWLPropertyExpressionVisitor):
            visitor.visit(self)
        elif isinstance(visitor, OWLPropertyExpressionVisitorEx):
            return visitor.visit(self)
        else:
            return super().accept(visitor)

    @staticmethod
    def is_data_property_expression():
        return False

    def as_data_property_expression(self):
        if self.is_data_property_expression():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLDataPropertyExpression' % str(type(self)))

    @staticmethod
    def is_object_property_expression():
        return False

    def as_object_property_expression(self):
        if self.is_object_property_expression():
            return self
        else:
            raise ClassCastException(
                '%s is not an OWLObjectPropertyExpression' % str(type(self)))

    @staticmethod
    def is_owl_top_object_property():
        """
        Determines if this is the owl:topObjectProperty.

        :return: Boolean indicating whether this property is
        owl:topObjectProperty.
        """
        return False

    @staticmethod
    def is_owl_bottom_object_property():
        """
        Determines if this is the owl:bottomObjectProperty.

        :return: Boolean indicating whether this property is
        owl:bottomObjectProperty
        """
        return False

    @staticmethod
    def is_owl_top_data_property():
        """
        Determines if this is the owl:topDataProperty.

        :return: Boolean indicating whether this property is owl:topDataProperty
        """
        return False

    @staticmethod
    def is_owl_bottom_data_property():
        """
        Determines if this is the owl:bottomDataProperty.

        :return: Boolean indicating whether this property is
        owl:bottomDataProperty
        """
        return False
