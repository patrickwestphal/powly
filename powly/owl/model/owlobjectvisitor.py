from abc import abstractmethod, ABC

from model.owlannotationobjectvisitor import OWLAnnotationObjectVisitor
from model.owlaxiomvisitor import OWLAxiomVisitor
from model.owlclassexpressionvisitor import OWLClassExpressionVisitor
from model.owldatavisitor import OWLDataVisitor
from model.owlindividualvisitor import OWLIndividualVisitor
from model.owllogicalaxiomvisitor import OWLLogicalAxiomVisitor
from model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from model.owlpropertyexpressionvisitor import OWLPropertyExpressionVisitor
from model.swrlobjectvisitor import SWRLObjectVisitor


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
