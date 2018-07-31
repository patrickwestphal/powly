from abc import abstractmethod

from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlaxiom import OWLAxiom


class OWLNaryAxiom(OWLAxiom, HasOperands):
    """
    Represents an axiom that contains two or more operands that could also be
    represented with multiple pairwise axioms.
    """
    @abstractmethod
    def operands(self):
        """
        :return: a stream of all operands for this n-ary axiom. This provides a
        platform for common operations across different types, e.g., this will
        be the properties() stream for a DisjointObjectProperties, or a
        classExpressions() stream for a DisjointClasses.
        """
        pass

    @abstractmethod
    def as_pairwise_axioms(self):
        """
        Gets this axiom as a set of pairwise axioms. Note that annotations on
        this axiom will not be copied to each axiom returned in the set of
        pairwise axioms.

        Note: This will contain all pairs, i.e., for the set "a, b, c" the
        pairs "a, b", "a, c", "b, c" will be returned. For some applications,
        only "a, b", "b, c" are required.

        :return: A collection of OWLNaryAxiom objects
        """
        pass

    # ... TODO: Finish
