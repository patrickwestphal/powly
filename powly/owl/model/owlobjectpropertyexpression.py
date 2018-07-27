from abc import abstractmethod, ABC

from powly.owl.model.swrlpredicate import SWRLPredicate
from powly.owl.model.owlpropertyexpression import OWLPropertyExpression


class OWLObjectPropertyExpression(OWLPropertyExpression, SWRLPredicate, ABC):
    @abstractmethod
    def get_inverse_property(self):
        """
        Obtains the property that corresponds to the inverse of this property.

        :return: An OWLObjectPropertyExpression object representing the inverse
        of this object property
        """

    def get_simplified(self):
        """
        Returns this property in its simplified form.

        :return: Let p be a property name and PE an object property expression.
        The simplification, 'simp', is defined as follows:
            simp(p) = p
            simp(inv(p)) = inv(p)
            simp(inv(inv(PE)) = simp(PE)
        """
        return self

    @abstractmethod
    def get_named_property(self):
        """
        Get the named object property used in this property expression.

        :return: P if this expression is either inv(P) or P.
        """
        pass

    @staticmethod
    def is_object_property_expression():
        return True
