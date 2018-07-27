from enum import Enum
from rdflib.term import URIRef

from vocab.namespaces import Namespaces


class ClassExpressionType(Enum):
    OWL_CLASS = 'Class'
    OBJECT_SOME_VALUES_FROM = 'ObjectSomeValuesFrom'
    OBJECT_ALL_VALUES_FROM = 'ObjectAllValuesFrom'
    OBJECT_MIN_CARDINALITY = 'ObjectMinCardinality'
    OBJECT_MAX_CARDINALITY = 'ObjectMaxCardinality'
    OBJECT_EXACT_CARDINALITY = 'ObjectExactCardinality'
    OBJECT_HAS_VALUE = 'ObjectHasValue'
    OBJECT_HAS_SELF = 'ObjectHasSelf'
    DATA_SOME_VALUES_FROM = 'DataSomeValuesFrom'
    DATA_ALL_VALUES_FROM = 'DataAllValuesFrom'
    DATA_MIN_CARDINALITY = 'DataMinCardinality'
    DATA_MAX_CARDINALITY = 'DataMaxCardinality'
    DATA_EXACT_CARDINALITY = 'DataExactCardinality'
    DATA_HAS_VALUE = 'DataHasValue'
    OBJECT_INTERSECTION_OF = 'ObjectIntersectionOf'
    OBJECT_UNION_OF = 'ObjectUnionOf'
    OBJECT_COMPLEMENT_OF = 'ObjectComplementOf'
    OBJECT_ONE_OF = 'ObjectOneOf'

    def __init__(self, name):
        """
        :param name: A string
        """
        self.name_ = name
        self.prefixed_name = Namespaces.OWL.prefix + ':' + name
        self.iri = URIRef(Namespaces.OWL.ns + name)

    def __str__(self):
        return self.name_

    def __repr__(self):
        return str(self)
