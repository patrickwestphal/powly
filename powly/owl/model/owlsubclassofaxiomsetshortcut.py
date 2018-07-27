from abc import abstractmethod, ABC


class OWLSubClassOfAxiomSetShortCut(ABC):
    """
    A marker interface for an axiom that can be represented by a set of
    SubClassOf axioms that is equivalent to this axiom.
    """
    @abstractmethod
    def as_owl_sub_class_of_axioms(self):
        """
        :return: the set of OWLSubClassOfAxiom objects equivalent to this
        expression
        """
        pass
