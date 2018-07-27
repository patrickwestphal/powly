from abc import abstractmethod, ABC

from powly.owl.model.swrlrulevisitorbase import SWRLRuleVisitorBase


class OWLLogicalAxiomVisitor(SWRLRuleVisitorBase, ABC):
    @abstractmethod
    def visit(self, axiom):
        """
        :param axiom: An object of one of the following classes:
        OWLAsymmetricObjectPropertyAxiom, OWLClassAssertionAxiom,
        OWLDataPropertyAssertionAxiom, OWLDataPropertyDomainAxiom,
        OWLDataPropertyRangeAxiom, OWLDifferentIndividualsAxiom,
        OWLDisjointClassesAxiom, OWLDisjointDataPropertiesAxiom,
        OWLDisjointObjectPropertiesAxiom, OWLDisjointUnionAxiom,
        OWLEquivalentClassesAxiom, OWLEquivalentDataPropertiesAxiom,
        OWLEquivalentObjectPropertiesAxiom, OWLFunctionalDataPropertyAxiom,
        OWLFunctionalObjectPropertyAxiom, OWLHasKeyAxiom,
        OWLInverseFunctionalObjectPropertyAxiom,
        OWLInverseObjectPropertiesAxiom, OWLIrreflexiveObjectPropertyAxiom,
        OWLNegativeDataPropertyAssertionAxiom,
        OWLNegativeObjectPropertyAssertionAxiom,
        OWLObjectPropertyAssertionAxiom, OWLObjectPropertyDomainAxiom,
        OWLObjectPropertyRangeAxiom, OWLReflexiveObjectPropertyAxiom,
        OWLSameIndividualAxiom, OWLSubClassOfAxiom, OWLSubDataPropertyOfAxiom,
        OWLSubObjectPropertyOfAxiom, OWLSubPropertyChainOfAxiom,
        OWLSymmetricObjectPropertyAxiom, OWLTransitiveObjectPropertyAxiom; or
        one of these classes: SWRLRule
        """
        pass
