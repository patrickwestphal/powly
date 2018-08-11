from abc import ABC, abstractmethod

from powly.owl.model.hasproperty import HasProperty
from powly.owl.model.owlrestriction import OWLRestriction


class OWLDataRestriction(OWLRestriction, HasProperty, ABC):
    """
    Represents a restriction (
    <a href="http://www.w3.org/TR/2009/REC-owl2-syntax-20091027/#Object_Property_Restrictions">Object Property Restriction</a>
    or
    <a href="http://www.w3.org/TR/2009/REC-owl2-syntax-20091027/#Data_Property_Restrictions">Data Property Restriction</a>)
    in the OWL 2 specification.
    """
    @abstractmethod
    def get_property(self):
        """
        :return: An OWLDataPropertyExpression object
        """
        pass

    @staticmethod
    def is_data_restriction():
        return True
