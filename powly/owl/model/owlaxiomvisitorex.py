from abc import abstractmethod, ABC

from model.owlannotationaxiomvisitorex import OWLAnnotationAxiomVisitorEx
from model.owllogicalaxiomvisitorex import OWLLogicalAxiomVisitorEx
from model.swrlrulevisitorexbase import SWRLRuleVisitorExBase


class OWLAxiomVisitorEx(
        OWLAnnotationAxiomVisitorEx, OWLLogicalAxiomVisitorEx,
        SWRLRuleVisitorExBase, ABC):

    @abstractmethod
    def visit(self, axiom):
        """
        :param axiom: An object of one of the following classes:
        OWLDatatypeDefinitionAxiom, OWLDeclarationAxiom; or of one of these
        classes: OWLAnnotationAssertionAxiom, OWLAnnotationPropertyDomainAxiom,
        OWLAnnotationPropertyRangeAxiom, OWLAsymmetricObjectPropertyAxiom,
        OWLClassAssertionAxiom, OWLDataPropertyAssertionAxiom,
        OWLDataPropertyDomainAxiom, OWLDataPropertyRangeAxiom,
        OWLDifferentIndividualsAxiom, OWLDisjointClassesAxiom,
        OWLDisjointDataPropertiesAxiom, OWLDisjointObjectPropertiesAxiom,
        OWLDisjointUnionAxiom, OWLEquivalentClassesAxiom,
        OWLEquivalentDataPropertiesAxiom, OWLEquivalentObjectPropertiesAxiom,
        OWLFunctionalDataPropertyAxiom, OWLFunctionalObjectPropertyAxiom,
        OWLHasKeyAxiom, OWLInverseFunctionalObjectPropertyAxiom,
        OWLInverseObjectPropertiesAxiom, OWLIrreflexiveObjectPropertyAxiom,
        OWLNegativeDataPropertyAssertionAxiom,
        OWLNegativeObjectPropertyAssertionAxiom,
        OWLObjectPropertyAssertionAxiom, OWLObjectPropertyDomainAxiom,
        OWLObjectPropertyRangeAxiom, OWLReflexiveObjectPropertyAxiom,
        OWLSameIndividualAxiom, OWLSubAnnotationPropertyOfAxiom,
        OWLSubClassOfAxiom, OWLSubDataPropertyOfAxiom,
        OWLSubObjectPropertyOfAxiom, OWLSubPropertyChainOfAxiom,
        OWLSymmetricObjectPropertyAxiom, OWLTransitiveObjectPropertyAxiom,
        SWRLRule
        """
        pass
