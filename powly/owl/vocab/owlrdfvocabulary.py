from enum import Enum

from rdflib.term import URIRef

from vocab.namespaces import Namespaces


class OWLRDFVocabulary(Enum):
    OWL_THING = (Namespaces.OWL, 'Thing')
    OWL_NOTHING = (Namespaces.OWL, 'Nothing')
    OWL_CLASS = (Namespaces.OWL, 'Class')
    OWL_ONTOLOGY = (Namespaces.OWL, 'Ontology')
    OWL_IMPORTS = (Namespaces.OWL, 'imports')
    OWL_VERSION_IRI = (Namespaces.OWL, 'versionIRI')
    OWL_VERSION_INFO = (Namespaces.OWL, 'versionInfo')
    OWL_EQUIVALENT_CLASS = (Namespaces.OWL, 'equivalentClass')
    OWL_OBJECT_PROPERTY = (Namespaces.OWL, 'ObjectProperty')
    OWL_DATA_PROPERTY = (Namespaces.OWL, 'DatatypeProperty')
    OWL_FUNCTIONAL_PROPERTY = (Namespaces.OWL, 'FunctionalProperty')
    OWL_ASYMMETRIC_PROPERTY = (Namespaces.OWL, 'AsymmetricProperty')
    OWL_SYMMETRIC_PROPERTY = (Namespaces.OWL, 'SymmetricProperty')
    OWL_RESTRICTION = (Namespaces.OWL, 'Restriction')
    OWL_ON_PROPERTY = (Namespaces.OWL, 'onProperty')
    OWL_INTERSECTION_OF = (Namespaces.OWL, 'intersectionOf')
    OWL_UNION_OF = (Namespaces.OWL, 'unionOf')
    OWL_ALL_VALUES_FROM = (Namespaces.OWL, 'allValuesFrom')
    OWL_SOME_VALUES_FROM = (Namespaces.OWL, 'someValuesFrom')
    OWL_HAS_VALUE = (Namespaces.OWL, 'hasValue')
    OWL_DISJOINT_WITH = (Namespaces.OWL, 'disjointWith')
    OWL_ONE_OF = (Namespaces.OWL, 'oneOf')
    OWL_HAS_SELF = (Namespaces.OWL, 'hasSelf')
    OWL_DISJOINT_UNION_OF = (Namespaces.OWL, 'disjointUnionOf')
    OWL_MIN_CARDINALITY = (Namespaces.OWL, 'minCardinality')
    OWL_CARDINALITY = (Namespaces.OWL, 'cardinality')
    OWL_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'qualifiedCardinality')
    OWL_ANNOTATION_PROPERTY = (Namespaces.OWL, 'AnnotationProperty')
    OWL_ANNOTATION = (Namespaces.OWL, 'Annotation')
    OWL_INDIVIDUAL = (Namespaces.OWL, 'Individual')
    OWL_NAMED_INDIVIDUAL = (Namespaces.OWL, 'NamedIndividual')
    OWL_DATATYPE = (Namespaces.OWL, 'Datatype')
    RDFS_SUBCLASS_OF = (Namespaces.RDFS, 'subClassOf')
    RDFS_SUB_PROPERTY_OF = (Namespaces.RDFS, 'subPropertyOf')
    RDF_TYPE = (Namespaces.RDF, 'type')
    RDF_NIL = (Namespaces.RDF, 'nil')
    RDF_REST = (Namespaces.RDF, 'rest')
    RDF_FIRST = (Namespaces.RDF, 'first')
    RDF_LIST = (Namespaces.RDF, 'List')
    OWL_MAX_CARDINALITY = (Namespaces.OWL, 'maxCardinality')
    RDFS_LABEL = (Namespaces.RDFS, 'label')
    RDFS_COMMENT = (Namespaces.RDFS, 'comment')
    RDFS_SEE_ALSO = (Namespaces.RDFS, 'seeAlso')
    RDFS_IS_DEFINED_BY = (Namespaces.RDFS, 'isDefinedBy')
    RDFS_RESOURCE = (Namespaces.RDFS, 'Resource')
    RDFS_LITERAL = (Namespaces.RDFS, 'Literal')
    RDFS_DATATYPE = (Namespaces.RDFS, 'Datatype')
    OWL_TRANSITIVE_PROPERTY = (Namespaces.OWL, 'TransitiveProperty')
    OWL_REFLEXIVE_PROPERTY = (Namespaces.OWL, 'ReflexiveProperty')
    OWL_IRREFLEXIVE_PROPERTY = (Namespaces.OWL, 'IrreflexiveProperty')
    OWL_INVERSE_OF = (Namespaces.OWL, 'inverseOf')
    OWL_COMPLEMENT_OF = (Namespaces.OWL, 'complementOf')
    OWL_DATATYPE_COMPLEMENT_OF = (Namespaces.OWL, 'datatypeComplementOf')
    OWL_ALL_DIFFERENT = (Namespaces.OWL, 'AllDifferent')
    OWL_DISTINCT_MEMBERS = (Namespaces.OWL, 'distinctMembers')
    OWL_SAME_AS = (Namespaces.OWL, 'sameAs')
    OWL_DIFFERENT_FROM = (Namespaces.OWL, 'differentFrom')
    OWL_DEPRECATED_PROPERTY = (Namespaces.OWL, 'DeprecatedProperty')
    OWL_EQUIVALENT_PROPERTY = (Namespaces.OWL, 'equivalentProperty')
    OWL_DEPRECATED_CLASS = (Namespaces.OWL, 'DeprecatedClass')
    OWL_DATA_RANGE = (Namespaces.OWL, 'DataRange')
    RDFS_DOMAIN = (Namespaces.RDFS, 'domain')
    RDFS_RANGE = (Namespaces.RDFS, 'range')
    RDFS_CLASS = (Namespaces.RDFS, 'Class')
    RDF_PROPERTY = (Namespaces.RDF, 'Property')
    OWL_PRIOR_VERSION = (Namespaces.OWL, 'priorVersion')
    OWL_DEPRECATED = (Namespaces.OWL, 'deprecated')
    OWL_INCOMPATIBLE_WITH = (Namespaces.OWL, 'incompatibleWith')
    OWL_PROPERTY_DISJOINT_WITH = (Namespaces.OWL, 'propertyDisjointWith')
    OWL_ON_CLASS = (Namespaces.OWL, 'onClass')
    OWL_ON_DATA_RANGE = (Namespaces.OWL, 'onDataRange')
    OWL_ON_DATA_TYPE = (Namespaces.OWL, 'onDatatype')
    OWL_WITH_RESTRICTIONS = (Namespaces.OWL, 'withRestrictions')
    OWL_AXIOM = (Namespaces.OWL, 'Axiom')
    OWL_PROPERTY_CHAIN_AXIOM = (Namespaces.OWL, 'propertyChainAxiom')
    OWL_ALL_DISJOINT_CLASSES = (Namespaces.OWL, 'AllDisjointClasses')
    OWL_MEMBERS = (Namespaces.OWL, 'members')
    OWL_ALL_DISJOINT_PROPERTIES = (Namespaces.OWL, 'AllDisjointProperties')
    OWL_TOP_OBJECT_PROPERTY = (Namespaces.OWL, 'topObjectProperty')
    OWL_BOTTOM_OBJECT_PROPERTY = (Namespaces.OWL, 'bottomObjectProperty')
    OWL_TOP_DATA_PROPERTY = (Namespaces.OWL, 'topDataProperty')
    OWL_BOTTOM_DATA_PROPERTY = (Namespaces.OWL, 'bottomDataProperty')
    OWL_HAS_KEY = (Namespaces.OWL, 'hasKey')
    OWL_ANNOTATED_SOURCE = (Namespaces.OWL, 'annotatedSource')
    OWL_ANNOTATED_PROPERTY = (Namespaces.OWL, 'annotatedProperty')
    OWL_ANNOTATED_TARGET = (Namespaces.OWL, 'annotatedTarget')
    OWL_SOURCE_INDIVIDUAL = (Namespaces.OWL, 'sourceIndividual')
    OWL_ASSERTION_PROPERTY = (Namespaces.OWL, 'assertionProperty')
    OWL_TARGET_INDIVIDUAL = (Namespaces.OWL, 'targetIndividual')
    OWL_TARGET_VALUE = (Namespaces.OWL, 'targetValue')

    OWL_INVERSE_FUNCTIONAL_PROPERTY = \
        (Namespaces.OWL, 'InverseFunctionalProperty')
    OWL_MIN_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'minQualifiedCardinality')
    OWL_MAX_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'maxQualifiedCardinality')
    OWL_NEGATIVE_PROPERTY_ASSERTION = \
        (Namespaces.OWL, 'NegativePropertyAssertion')
    RDF_LANG_STRING = (Namespaces.RDF, 'langString')
    RDF_PLAIN_LITERAL = (Namespaces.RDF, 'PlainLiteral')
    RDF_DESCRIPTION = (Namespaces.RDF, 'Description')
    RDF_XML_LITERAL = (Namespaces.RDF, 'XMLLiteral')
    OWL_BACKWARD_COMPATIBLE_WITH = (Namespaces.OWL, 'backwardCompatibleWith')
    OWL_INVERSE_OBJECT_PROPERTY_EXPRESSION = \
        (Namespaces.OWL, 'inverseObjectPropertyExpression')

    OWL_ONTOLOGY_PROPERTY = (Namespaces.OWL, 'OntologyProperty')
    OWL_ANTI_SYMMETRIC_PROPERTY = (Namespaces.OWL, 'AntisymmetricProperty')
    OWL_DATA_RESTRICTION = (Namespaces.OWL, 'DataRestriction')
    OWL_OBJECT_RESTRICTION = (Namespaces.OWL, 'ObjectRestriction')
    OWL_SELF_RESTRICTION = (Namespaces.OWL, 'SelfRestriction')
    OWL_DECLARED_AS = (Namespaces.OWL, 'declaredAs')
    OWL_NEGATIVE_OBJECT_PROPERTY_ASSERTION = \
        (Namespaces.OWL, 'NegativeObjectPropertyAssertion')
    OWL_NEGATIVE_DATA_PROPERTY_ASSERTION = \
        (Namespaces.OWL, 'NegativeDataPropertyAssertion')
    RDF_SUBJECT = (Namespaces.RDF, 'subject')
    RDF_PREDICATE = (Namespaces.RDF, 'predicate')
    RDF_OBJECT = (Namespaces.RDF, 'object')
    OWL_SUBJECT = (Namespaces.OWL, 'subject')
    OWL_PREDICATE = (Namespaces.OWL, 'predicate')
    OWL_OBJECT = (Namespaces.OWL, 'object')
    OWL_OBJECT_PROPERTY_DOMAIN = (Namespaces.OWL, 'objectPropertyDomain')
    OWL_DATA_PROPERTY_DOMAIN = (Namespaces.OWL, 'dataPropertyDomain')
    OWL_DATA_PROPERTY_RANGE = (Namespaces.OWL, 'dataPropertyRange')
    OWL_OBJECT_PROPERTY_RANGE = (Namespaces.OWL, 'objectPropertyRange')
    OWL_SUB_OBJECT_PROPERTY_OF = (Namespaces.OWL, 'subObjectPropertyOf')
    OWL_SUB_DATA_PROPERTY_OF = (Namespaces.OWL, 'subDataPropertyOf')
    OWL_DISJOINT_DATA_PROPERTIES = (Namespaces.OWL, 'disjointDataProperties')
    OWL_DISJOINT_OBJECT_PROPERTIES = \
        (Namespaces.OWL, 'disjointObjectProperties')
    OWL_EQUIVALENT_DATA_PROPERTIES = (Namespaces.OWL, 'equivalentDataProperty')
    OWL_EQUIVALENT_OBJECT_PROPERTIES = \
        (Namespaces.OWL, 'equivalentObjectProperty')
    OWL_FUNCTIONAL_DATA_PROPERTY = (Namespaces.OWL, 'FunctionalDataProperty')
    OWL_FUNCTIONAL_OBJECT_PROPERTY = \
        (Namespaces.OWL, 'FunctionalObjectProperty')
    OWL_PROPERTY_CHAIN = (Namespaces.OWL, 'propertyChain')

    def __init__(self, namespace, short_name):
        """
        :param namespace: A Namespaces object
        :param short_name: A string
        """
        self.namespace = namespace
        self.short_name = short_name
        self.prefixed_name = namespace.prefix + ':' + short_name
        self.iri = URIRef(str(namespace) + short_name)
        self.uri = self.iri

    def __str__(self):
        return str(self.iri)

    @classmethod
    def built_in_ap_iris(cls):
        return map(lambda e: e.uri, {
            cls.RDFS_LABEL, cls.RDFS_COMMENT, cls.OWL_VERSION_INFO,
            cls.OWL_BACKWARD_COMPATIBLE_WITH, cls.OWL_PRIOR_VERSION,
            cls.RDFS_SEE_ALSO, cls.RDFS_IS_DEFINED_BY,
            cls.OWL_INCOMPATIBLE_WITH, cls.OWL_DEPRECATED})
