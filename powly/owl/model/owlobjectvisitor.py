from abc import abstractmethod, ABC

from powly.owl.model.owlannotationobjectvisitor import OWLAnnotationObjectVisitor
from powly.owl.model.owlaxiomvisitor import OWLAxiomVisitor
from powly.owl.model.owlclassexpressionvisitor import OWLClassExpressionVisitor
from powly.owl.model.owldatavisitor import OWLDataVisitor
from powly.owl.model.owlindividualvisitor import OWLIndividualVisitor
from powly.owl.model.owllogicalaxiomvisitor import OWLLogicalAxiomVisitor
from powly.owl.model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from powly.owl.model.owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor
from powly.owl.model.swrlobjectvisitor import SWRLObjectVisitor


class OWLObjectVisitor(
        OWLAnnotationObjectVisitor, OWLAxiomVisitor, OWLClassExpressionVisitor,
        OWLDataVisitor, OWLIndividualVisitor, OWLLogicalAxiomVisitor,
        OWLNamedObjectVisitor, OWLPropertyExpressionVisitor, SWRLObjectVisitor,
        ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of these classes:
        IRI, OWLAnnotation, OWLAnnotationAssertionAxiom, OWLAnnotationProperty,
        OWLAnnotationPropertyDomainAxiom, OWLAnnotationPropertyRangeAxiom,
        OWLAnonymousIndividual, OWLAsymmetricObjectPropertyAxiom, OWLClass,
        OWLClassAssertionAxiom, OWLDataAllValuesFrom, OWLDataComplementOf,
        OWLDataExactCardinality, OWLDataHasValue, OWLDataIntersectionOf,
        OWLDataMaxCardinality, OWLDataMinCardinality, OWLDataOneOf,
        OWLDataProperty, OWLDataPropertyAssertionAxiom,
        OWLDataPropertyDomainAxiom, OWLDataPropertyRangeAxiom,
        OWLDataSomeValuesFrom, OWLDatatype, OWLDatatypeDefinitionAxiom,
        OWLDatatypeRestriction, OWLDataUnionOf, OWLDeclarationAxiom,
        OWLDifferentIndividualsAxiom, OWLDisjointClassesAxiom,
        OWLDisjointDataPropertiesAxiom, OWLDisjointObjectPropertiesAxiom,
        OWLDisjointUnionAxiom, OWLEquivalentClassesAxiom,
        OWLEquivalentDataPropertiesAxiom, OWLEquivalentObjectPropertiesAxiom,
        OWLFacetRestriction, OWLFunctionalDataPropertyAxiom,
        OWLFunctionalObjectPropertyAxiom, OWLHasKeyAxiom,
        OWLInverseFunctionalObjectPropertyAxiom,
        OWLInverseObjectPropertiesAxiom, OWLIrreflexiveObjectPropertyAxiom,
        OWLLiteral, OWLNamedIndividual, OWLNegativeDataPropertyAssertionAxiom,
        OWLNegativeObjectPropertyAssertionAxiom, OWLObjectAllValuesFrom,
        OWLObjectComplementOf, OWLObjectExactCardinality, OWLObjectHasSelf,
        OWLObjectHasValue, OWLObjectIntersectionOf, OWLObjectInverseOf,
        OWLObjectMaxCardinality, OWLObjectMinCardinality, OWLObjectOneOf,
        OWLObjectProperty, OWLObjectPropertyAssertionAxiom,
        OWLObjectPropertyDomainAxiom, OWLObjectPropertyRangeAxiom,
        OWLObjectSomeValuesFrom, OWLObjectUnionOf, OWLOntology,
        OWLReflexiveObjectPropertyAxiom, OWLSameIndividualAxiom,
        OWLSubAnnotationPropertyOfAxiom, OWLSubClassOfAxiom,
        OWLSubDataPropertyOfAxiom, OWLSubObjectPropertyOfAxiom,
        OWLSubPropertyChainOfAxiom, OWLSymmetricObjectPropertyAxiom,
        OWLTransitiveObjectPropertyAxiom, SWRLBuiltInAtom, SWRLClassAtom,
        SWRLDataPropertyAtom, SWRLDataRangeAtom, SWRLDifferentIndividualsAtom,
        SWRLIndividualArgument, SWRLLiteralArgument, SWRLObjectPropertyAtom,
        SWRLSameIndividualAtom, SWRLVariable, SWRLRule
        """
        pass
