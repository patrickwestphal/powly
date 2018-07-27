from abc import ABC, abstractmethod

from powly.owl.model.owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor
from powly.owl.model.owlannotationvaluevisitor import OWLAnnotationValueVisitor
from powly.owl.model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from powly.owl.model.owlliteralvisitorbase import OWLLiteralVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


class OWLAnnotationObjectVisitor(
        OWLAnnotationAxiomVisitor, OWLAnnotationValueVisitor,
        OWLAnonymousIndividualVisitorBase, OWLLiteralVisitorBase,
        OWLVisitorBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes: OWLAnnotation;
        or one of these classes: IRI, OWLAnnotationAssertionAxiom,
        OWLAnnotationPropertyDomainAxiom, OWLAnnotationPropertyRangeAxiom,
        OWLAnonymousIndividual, OWLLiteral, OWLSubAnnotationPropertyOfAxiom
        """
        pass
