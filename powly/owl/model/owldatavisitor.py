from abc import ABC, abstractmethod

from powly.owl.model.owldatarangevisitor import OWLDataRangeVisitor
from powly.owl.model.owlliteralvisitorbase import OWLLiteralVisitorBase


class OWLDataVisitor(OWLDataRangeVisitor, OWLLiteralVisitorBase, ABC):
    """
    A visitor which can visit various data ranges and constants.
    """

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes:
        OWLFacetRestriction; or of these classes: OWLDataComplementOf,
        OWLDataIntersectionOf, OWLDataOneOf, OWLDataUnionOf
        OWLDatatypeRestriction, OWLDatatype, OWLLiteral
        """
        pass
