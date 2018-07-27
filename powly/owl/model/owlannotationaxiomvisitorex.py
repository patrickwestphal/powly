from abc import abstractmethod, ABC

from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLAnnotationAxiomVisitorEx(OWLVisitorExBase, ABC):
    @abstractmethod
    def visit(self, axiom):
        """
        :param axiom: An object of one of the following classes:
        OWLAnnotationAssertionAxiom, OWLAnnotationPropertyDomainAxiom,
        OWLAnnotationPropertyRangeAxiom, OWLSubAnnotationPropertyOfAxiom
        """
        pass
