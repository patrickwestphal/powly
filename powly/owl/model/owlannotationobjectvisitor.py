from abc import ABC, abstractmethod

from model.owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor
from model.owlannotationvaluevisitor import OWLAnnotationValueVisitor
from model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from model.owlliteralvisitorbase import OWLLiteralVisitorBase
from model.owlvisitorbase import OWLVisitorBase


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
