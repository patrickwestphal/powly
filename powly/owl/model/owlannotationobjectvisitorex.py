from abc import abstractmethod, ABC

from powly.owl.model.owlannotationaxiomvisitorex import OWLAnnotationAxiomVisitorEx
from powly.owl.model.owlannotationvaluevisitorex import OWLAnnotationValueVisitorEx
from powly.owl.model.owlanonymousindividualvisitorexbase import \
    OWLAnonymousIndividualVisitorExBase
from powly.owl.model.owlliteralvisitorexbase import OWLLiteralVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


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
