from abc import ABC, abstractmethod

from powly.owl.model.owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor
from powly.owl.model.owllogicalaxiomvisitor import OWLLogicalAxiomVisitor
from powly.owl.model.swrlrulevisitorbase import SWRLRuleVisitorBase


class OWLAxiomVisitor(
        OWLAnnotationAxiomVisitor, OWLLogicalAxiomVisitor, SWRLRuleVisitorBase,
        ABC):

    @abstractmethod
    def visit(self, axiom):
        """
        :param axiom: An object of one of the following classes:
        OWLDatatypeDefinitionAxiom, OWLDeclarationAxiom; or one of these
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
