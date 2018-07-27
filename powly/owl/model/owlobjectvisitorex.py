from abc import abstractmethod, ABC

from model.owlannotationobjectvisitorex import OWLAnnotationObjectVisitorEx
from model.owlaxiomvisitorex import OWLAxiomVisitorEx
from model.owlclassexpressionvisitorex import OWLClassExpressionVisitorEx
from model.owldatavisitorex import OWLDataVisitorEx
from model.owlindividualvisitorex import OWLIndividualVisitorEx
from model.owllogicalaxiomvisitorex import OWLLogicalAxiomVisitorEx
from model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from model.owlpropertyexpressionvisitorex import OWLPropertyExpressionVisitorEx
from model.swrlobjectvisitorex import SWRLObjectVisitorEx


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
