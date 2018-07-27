from abc import abstractmethod, ABC

from model.owlannotationaxiomvisitorex import OWLAnnotationAxiomVisitorEx
from model.owlannotationvaluevisitorex import OWLAnnotationValueVisitorEx
from model.owlanonymousindividualvisitorexbase import \
    OWLAnonymousIndividualVisitorExBase
from model.owlliteralvisitorexbase import OWLLiteralVisitorExBase
from model.owlvisitorexbase import OWLVisitorExBase


class OWLAnnotationObjectVisitorEx(
        OWLAnnotationAxiomVisitorEx, OWLAnnotationValueVisitorEx,
        OWLAnonymousIndividualVisitorExBase, OWLLiteralVisitorExBase,
        OWLVisitorExBase, ABC):

    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes: OWLAnnotation;
        or one of these classes: IRI, OWLAnnotationAssertionAxiom,
        OWLAnnotationPropertyDomainAxiom, OWLAnnotationPropertyRangeAxiom,
        OWLAnonymousIndividual, OWLLiteral, OWLSubAnnotationPropertyOfAxiom
        """
        pass
