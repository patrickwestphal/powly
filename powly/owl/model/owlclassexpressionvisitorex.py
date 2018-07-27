from abc import abstractmethod, ABC

from powly.owl.model.owlclassvisitorexbase import OWLClassVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLClassExpressionVisitorEx(
        OWLClassVisitorExBase,  OWLVisitorExBase, ABC):
    """
    An interface to objects that can visit OWLClassExpressions.
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
        OWLObjectUnionOf; or one of these classes: OWLClass
        """
        pass
