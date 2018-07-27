from abc import ABC, abstractmethod

from powly.owl.model.owldataentityvisitorbase import OWLDataEntityVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


class OWLDataRangeVisitor(OWLDataEntityVisitorBase, OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes:
        OWLDataComplementOf, OWLDataIntersectionOf, OWLDataOneOf,
        OWLDatatypeRestriction, OWLDataUnionOf; or one of these classes:
        OWLDatatype
        """
        pass
