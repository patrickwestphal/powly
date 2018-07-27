from abc import abstractmethod, ABC

from powly.owl.model.owlclassvisitorbase import OWLClassVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


class OWLClassExpressionVisitor(OWLClassVisitorBase, OWLVisitorBase, ABC):
    """
    An interface to objects that can visit OWLClassExpressions. (See the
    Visitor Patterns)
    """

    @abstractmethod
    def visit(self, ce):
        """
        :param ce: An object of one of the following classes:
        OWLDataAllValuesFrom, OWLDataExactCardinality, OWLDataHasValue,
        OWLDataMaxCardinality, OWLDataMinCardinality, OWLDataSomeValuesFrom,
        OWLObjectAllValuesFrom, OWLObjectComplementOf,
        OWLObjectExactCardinality, OWLObjectHasSelf, OWLObjectHasValue,
        OWLObjectIntersectionOf, OWLObjectMaxCardinality,
        OWLObjectMinCardinality, OWLObjectOneOf, OWLObjectSomeValuesFrom,
        OWLObjectUnionOf
        """
        pass
