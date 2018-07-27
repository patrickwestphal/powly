from abc import abstractmethod, ABC

from model.owldataentityvisitorexbase import OWLDataEntityVisitorExBase
from model.owlliteralvisitorexbase import OWLLiteralVisitorExBase
from model.owlvisitorexbase import OWLVisitorExBase


class OWLDataVisitorEx(
        OWLDataEntityVisitorExBase, OWLLiteralVisitorExBase, OWLVisitorExBase,
        ABC):

    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes:
        OWLDataComplementOf, OWLDataIntersectionOf, OWLDataOneOf,
        OWLDatatypeRestriction, OWLDataUnionOf, OWLFacetRestriction; or one of
        these classes: OWLDatatype, OWLLiteral
        """
        pass
