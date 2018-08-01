from abc import ABC, abstractmethod


class OWLSubClassOfAxiomShortCut(ABC):
    @abstractmethod
    def as_owl_sub_class_of_axiom(self):
        """
        Gets this axiom as an OWLSubClassOfAxiom.

        :return: An OWLSubClassOfAxiom that is equivalent to this axiom.
        Note that annotations are not copied to the returned
        OWLSubClassOfAxiom axiom.
        """
        pass
