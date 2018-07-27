from abc import abstractmethod, ABC

from powly.owl.model.owlanonymousclassexpression import OWLAnonymousClassExpression


class OWLRestriction(OWLAnonymousClassExpression, ABC):
    """
    Represents a restriction (Object Property Restriction or Data Property
    Restriction) in the OWL 2 specification.
    """

    @abstractmethod
    def get_property(self):
        """
        :return: An OWLPropertyExpression object
        """
        pass

    @staticmethod
    def is_data_restriction():
        """
        Determines if this is a data restriction.

        :return: Boolean indicating whether this expression is a data
        restriction
        """
        return False

    @staticmethod
    def is_object_restriction():
        """
        Determines if this is an object restriction.

        :return: Boolean indicating whether this expression is an object
        restriction
        """
        return False
