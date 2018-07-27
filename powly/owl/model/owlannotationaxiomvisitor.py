from abc import abstractmethod, ABC

from model.owlvisitorbase import OWLVisitorBase


class OWLAnnotationAxiomVisitor(OWLVisitorBase, ABC):
    """
    A visitor which visits the different kinds of annotation axioms.
    """

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes:
        OWLAnnotationAssertionAxiom, OWLAnnotationPropertyDomainAxiom,
        OWLAnnotationPropertyRangeAxiom, OWLSubAnnotationPropertyOfAxiom
        """
        pass
