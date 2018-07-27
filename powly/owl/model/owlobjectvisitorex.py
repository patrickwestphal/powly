from abc import abstractmethod, ABC

from powly.owl.model.owlannotationobjectvisitorex import OWLAnnotationObjectVisitorEx
from powly.owl.model.owlaxiomvisitorex import OWLAxiomVisitorEx
from powly.owl.model.owlclassexpressionvisitorex import OWLClassExpressionVisitorEx
from powly.owl.model.owldatavisitorex import OWLDataVisitorEx
from powly.owl.model.owlindividualvisitorex import OWLIndividualVisitorEx
from powly.owl.model.owllogicalaxiomvisitorex import OWLLogicalAxiomVisitorEx
from powly.owl.model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from powly.owl.model.owlpropertyexpressionvisitorex import OWLPropertyExpressionVisitorEx
from powly.owl.model.swrlobjectvisitorex import SWRLObjectVisitorEx


class OWLObjectVisitorEx(
        OWLAnnotationObjectVisitorEx, OWLAxiomVisitorEx,
        OWLClassExpressionVisitorEx, OWLLogicalAxiomVisitorEx, OWLDataVisitorEx,
        OWLIndividualVisitorEx, OWLNamedObjectVisitorEx,
        OWLPropertyExpressionVisitorEx, SWRLObjectVisitorEx, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of these classes: IRI, OWLAnnotation,
        OWLAnnotationAssertionAxiom, OWLAnnotationProperty,
        OWLAnnotationPropertyDomainAxiom, OWLAnnotationPropertyRangeAxiom,
        OWLAnonymousIndividual, OWLAsymmetricObjectPropertyAxiom,
        OWLDatatypeDefinitionAxiom, OWLClass, OWLClassAssertionAxiom,
        OWLDataAllValuesFrom, OWLDataComplementOf, OWLDataExactCardinality,
        OWLDataHasValue, OWLDataIntersectionOf, OWLDataMaxCardinality,
        OWLDataMinCardinality, OWLDataOneOf, OWLDataProperty,
        OWLDataPropertyAssertionAxiom, OWLDataPropertyDomainAxiom,
        OWLDataPropertyRangeAxiom, OWLDataSomeValuesFrom, OWLDatatype,
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
        OWLObjectSomeValuesFrom, OWLObjectUnionOf OWLOntology,
        OWLReflexiveObjectPropertyAxiom, OWLSameIndividualAxiom,
        OWLSubAnnotationPropertyOfAxiom, OWLSubClassOfAxiom,
        OWLSubDataPropertyOfAxiom, OWLSubObjectPropertyOfAxiom,
        OWLSubPropertyChainOfAxiom, OWLSymmetricObjectPropertyAxiom,
        OWLTransitiveObjectPropertyAxiom, SWRLBuiltInAtom, SWRLClassAtom,
        SWRLDataPropertyAtom, SWRLDataRangeAtom, SWRLDifferentIndividualsAtom,
        SWRLIndividualArgument, SWRLLiteralArgument, SWRLObjectPropertyAtom,
        SWRLRule, SWRLSameIndividualAtom, SWRLVariable
        """
        pass
