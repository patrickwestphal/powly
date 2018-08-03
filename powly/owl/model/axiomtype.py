import itertools

from powly.owl.model.owlannotationassertionaxiom import \
    OWLAnnotationAssertionAxiom
from powly.owl.model.owlclassassertionaxiom import OWLClassAssertionAxiom
from powly.owl.model.owldatapropertydomainaxiom import \
    OWLDataPropertyDomainAxiom
from powly.owl.model.owldatapropertyrangeaxiom import OWLDataPropertyRangeAxiom
from powly.owl.model.owldeclarationaxiom import OWLDeclarationAxiom
from powly.owl.model.owldifferentindividualsaxiom import \
    OWLDifferentIndividualsAxiom
from powly.owl.model.owldisjointclassesaxiom import OWLDisjointClassesAxiom
from powly.owl.model.owldisjointunionaxiom import OWLDisjointUnionAxiom
from powly.owl.model.owlequivalentclassesaxiom import OWLEquivalentClassesAxiom
from powly.owl.model.owlinverseobjectpropertiesaxiom import \
    OWLInverseObjectPropertiesAxiom
from powly.owl.model.owlobjectpropertydomainaxiom import \
    OWLObjectPropertyDomainAxiom
from powly.owl.model.owlsubclassofaxiom import OWLSubClassOfAxiom
from powly.owl.model.owlsubobjectpropertyofaxiom import \
    OWLSubObjectPropertyOfAxiom


class AxiomType(object):
    @classmethod
    def get_instance(
            cls, actual_class, index, name, owl2_axiom,
            non_syntactic_owl2_axiom, is_logical):
        """
        :param actual_class: A class
        :param index: An integer object
        :param name: A string
        :param owl2_axiom: A Boolean
        :param non_syntactic_owl2_axiom: A Boolean
        :param is_logical: A Boolean
        :return:
        """
        return cls(
            actual_class, index, name, owl2_axiom, non_syntactic_owl2_axiom,
            is_logical)

    DECLARATION = get_instance(
        type(OWLDeclarationAxiom), 0, 'Declaration', True, True, False)
    EQUIVALENT_CLASSES = get_instance(
        type(OWLEquivalentClassesAxiom), 1, 'EquivalentClasses', False, False,
        True)
    SUBCLASS_OF = get_instance(
        type(OWLSubClassOfAxiom), 2, 'SubClassOf', False, False, True)
    DISJOINT_CLASSES = get_instance(
        type(OWLDisjointClassesAxiom), 3, 'DisjointClasses', False, False, True)
    DISJOINT_UNION = get_instance(
        type(OWLDisjointUnionAxiom), 4, 'DisjointUnion', True, False, True)
    CLASS_ASSERTION = get_instance(
        type(OWLClassAssertionAxiom), 5, 'ClassAssertion', False, False, True)

    # TODO: Implement OWLSameIndividualAxiom
    # SAME_INDIVIDUAL = get_instance(
    #     type(OWLSameIndividualAxiom), 6, 'SameIndividual', False, False, True)

    DIFFERENT_INDIVIDUALS = get_instance(
        type(OWLDifferentIndividualsAxiom), 7, 'DifferentIndividuals', False,
        False, True)

    # TODO: Implement OWLObjectPropertyAssertionAxiom
    # OBJECT_PROPERTY_ASSERTION = get_instance(
    #     type(OWLObjectPropertyAssertionAxiom), 8, 'ObjectPropertyAssertion',
    #     False, False, True)

    # TODO: Implement OWLNegativeObjectPropertyAssertionAxiom
    # NEGATIVE_OBJECT_PROPERTY_ASSERTION = get_instance(
    #     type(OWLNegativeObjectPropertyAssertionAxiom), 9,
    #     'NegativeObjectPropertyAssertion', True, False, True)

    # TODO: Implement OWLDataPropertyAssertionAxiom
    # DATA_PROPERTY_ASSERTION = get_instance(
    #     type(OWLDataPropertyAssertionAxiom), 10, 'DataPropertyAssertion',
    #     False, False, True)

    # TODO: Implmenet OWLNegativeDataPropertyAssertionAxiom
    # NEGATIVE_DATA_PROPERTY_ASSERTION = get_instance(
    #     type(OWLNegativeDataPropertyAssertionAxiom), 11,
    #     'NegativeDataPropertyAssertion', True, False, True)

    # TODO: Implement OWLEquivalentObjectPropertiesAxiom
    # EQUIVALENT_OBJECT_PROPERTIES = get_instance(
    #     type(OWLEquivalentObjectPropertiesAxiom), 12,
    #     'EquivalentObjectProperties', False, False, True)

    SUB_OBJECT_PROPERTY = get_instance(
        type(OWLSubObjectPropertyOfAxiom), 13, 'SubObjectPropertyOf', False,
        False, True)

    INVERSE_OBJECT_PROPERTIES = get_instance(
        type(OWLInverseObjectPropertiesAxiom), 14, 'InverseObjectProperties',
        False, False, True)

    # TODO: Implment OWLFunctionalObjectPropertyAxiom
    # FUNCTIONAL_OBJECT_PROPERTY = get_instance(
    #     type(OWLFunctionalObjectPropertyAxiom), 15, 'FunctionalObjectProperty',
    #     False, False, True)

    # TODO: Implement OWLInverseFunctionalObjectPropertyAxiom
    # INVERSE_FUNCTIONAL_OBJECT_PROPERTY = get_instance(
    #     type(OWLInverseFunctionalObjectPropertyAxiom), 16,
    #     'InverseFunctionalObjectProperty', False, False, True)

    # TODO: Implement OWLSymmetricObjectPropertyAxiom
    # SYMMETRIC_OBJECT_PROPERTY = get_instance(
    #     type(OWLSymmetricObjectPropertyAxiom), 17, 'SymmetricObjectProperty',
    #     False, False, True)

    # TODO: Implment OWLAsymmetricObjectPropertyAxiom
    # ASYMMETRIC_OBJECT_PROPERTY = get_instance(
    #     type(OWLAsymmetricObjectPropertyAxiom), 18, 'AsymmetricObjectProperty',
    #     True, True, True)

    # TODO: Implement OWLTransitiveObjectPropertyAxiom
    # TRANSITIVE_OBJECT_PROPERTY = get_instance(
    #     type(OWLTransitiveObjectPropertyAxiom), 19, 'TransitiveObjectProperty',
    #     False, False, True)

    # TODO: Implement OWLReflexiveObjectPropertyAxiom
    # REFLEXIVE_OBJECT_PROPERTY = get_instance(
    #     type(OWLReflexiveObjectPropertyAxiom), 20, 'ReflexiveObjectProperty',
    #     True, True, True)

    # TODO: Implment OWLIrreflexiveObjectPropertyAxiom
    # IRREFLEXIVE_OBJECT_PROPERTY = get_instance(
    #     type(OWLIrreflexiveObjectPropertyAxiom), 21,
    #     'IrrefexiveObjectProperty', True, True, True)

    OBJECT_PROPERTY_DOMAIN = get_instance(
        type(OWLObjectPropertyDomainAxiom), 22, 'ObjectPropertyDomain', False,
        False, True)

    # TODO: Implement OWLObjectPropertyRangeAxiom
    # OBJECT_PROPERTY_RANGE = get_instance(
    #     type(OWLObjectPropertyRangeAxiom), 23, 'ObjectPropertyRange', False,
    #     False, True)

    # TODO: Implement OWLDisjointObjectPropertiesAxiom
    # DISJOINT_OBJECT_PROPERTIES = get_instance(
    #     type(OWLDisjointObjectPropertiesAxiom), 24, 'DisjointObjectProperties',
    #     True, True, True)

    # TODO: Implement OWLSubPropertyChainOfAxiom
    # SUB_PROPERTY_CHAIN_OF = get_instance(
    #     type(OWLSubPropertyChainOfAxiom), 25, 'SubPropertyChainOf', True, True,
    #     True)

    # TOOD: Implement OWLEquivalentDataPropertiesAxiom
    # EQUIVALENT_DATA_PROPERTIES = get_instance(
    #     type(OWLEquivalentDataPropertiesAxiom), 26, 'EquivalentDataProperties',
    #     False, False, True)

    # TODO: Implement OWLSubDataPropertyOfAxiom
    # SUB_DATA_PROPERTY = get_instance(
    #     type(OWLSubDataPropertyOfAxiom), 27, 'SubDataPropertyOf', False, False,
    #     True)

    # TODO: Implement OWLFunctionalDataPropertyAxiom
    # FUNCTIONAL_DATA_PROPERTY = get_instance(
    #     type(OWLFunctionalDataPropertyAxiom), 28, 'FunctionalDataProperty',
    #     False, False, True)

    DATA_PROPERTY_DOMAIN = get_instance(
        type(OWLDataPropertyDomainAxiom), 29, 'DataPropertyDomain', False,
        False, True)
    DATA_PROPERTY_RANGE = get_instance(
        type(OWLDataPropertyRangeAxiom), 30, 'DataPropertyRange', False, False,
        True)

    # TODO: Implement OWLDisjointDataPropertiesAxiom
    # DISJOINT_DATA_PROPERTIES = get_instance(
    #     type(OWLDisjointDataPropertiesAxiom), 31, 'DisjointDataProperties',
    #     True, True, True)

    # TODO: Implement OWLDatatypeDefinitionAxiom
    # DATATYPE_DEFINITION = get_instance(
    #     type(OWLDatatypeDefinitionAxiom), 38, 'DatatypeDefinition', True, True,
    #     True)

    # TODO: Implement OWLDatatypeDefinitionAxiom
    # HAS_KEY = get_instance(
    #     type(OWLHasKeyAxiom), 32, 'HasKey', True, True, True)

    # TODO: Implement SWRLRule
    # SWRL_RULE = get_instance(type(SWRLRule), 33, 'Rule', False, False, True)

    ANNOTATION_ASSERTION = get_instance(
        type(OWLAnnotationAssertionAxiom), 34, 'AnnotationAssertion', False,
        False, False)

    # TODO: Implement OWLSubAnnotationPropertyOfAxiom
    # SUB_ANNOTATION_PROPERTY_OF = get_instance(
    #     type(OWLSubAnnotationPropertyOfAxiom), 35, 'SubAnnotationPropertyOf',
    #     True, True, False)

    # TODO: Implement OWLAnnotationPropertyRangeAxiom
    # ANNOTATION_PROPERTY_RANGE = get_instance(
    #     type(OWLAnnotationPropertyRangeAxiom), 36, 'AnnotationPropertyRangeOf',
    #     True, True, False)

    # TODO: Implement OWLAnnotationPropertyDomainAxiom
    # ANNOTATION_PROPERTY_DOMAIN = get_instance(
    #     type(OWLAnnotationPropertyDomainAxiom), 37,
    #     'AnnotationPropertyDomain', True, True, False)

    AXIOM_TYPES = {
        SUBCLASS_OF, EQUIVALENT_CLASSES, DISJOINT_CLASSES, CLASS_ASSERTION,
        # SAME_INDIVIDUAL,  # TODO: Add when implemented
        DIFFERENT_INDIVIDUALS,
        # OBJECT_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # NEGATIVE_OBJECT_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # DATA_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # NEGATIVE_DATA_PROPERTY_ASSERTION,  # TODO: Add when implemented
        OBJECT_PROPERTY_DOMAIN,
        # OBJECT_PROPERTY_RANGE,  # TODO: Add when implemented
        # DISJOINT_OBJECT_PROPERTIES,  # TODO: Add when implemented
        SUB_OBJECT_PROPERTY,
        # EQUIVALENT_OBJECT_PROPERTIES,  # TODO: Add when implemented
        INVERSE_OBJECT_PROPERTIES,
        # SUB_PROPERTY_CHAIN_OF,  # TODO: Add when implemented
        # FUNCTIONAL_OBJECT_PROPERTY,  # TODO: Add when implemented
        # INVERSE_FUNCTIONAL_OBJECT_PROPERTY,  # TODO: Add when implemented
        # SYMMETRIC_OBJECT_PROPERTY,  # TODO: Add when implemented
        # ASYMMETRIC_OBJECT_PROPERTY,  # TODO: Add when implemented
        # TRANSITIVE_OBJECT_PROPERTY,  # TODO: Add when implemented
        # REFLEXIVE_OBJECT_PROPERTY,  # TODO: Add when implemented
        # IRREFLEXIVE_OBJECT_PROPERTY,  # TODO: Add when implemented
        DATA_PROPERTY_DOMAIN, DATA_PROPERTY_RANGE,
        #DISJOINT_DATA_PROPERTIES,  # TODO: Add when implemented
        #SUB_DATA_PROPERTY,  # TODO: Add when implemented
        #EQUIVALENT_DATA_PROPERTIES,  # TODO: Add when implemented
        #FUNCTIONAL_DATA_PROPERTY,  # TODO: Add when implemented
        #DATATYPE_DEFINITION,  # TODO: Add when implemented
        DISJOINT_UNION, DECLARATION,
        # SWRL_RULE,  # TODO: Add when implemented
        ANNOTATION_ASSERTION,
        # SUB_ANNOTATION_PROPERTY_OF,  # TODO: Add when implemented
        # ANNOTATION_PROPERTY_DOMAIN,  # TODO: Add when implemented
        # ANNOTATION_PROPERTY_RANGE,  # TODO: Add when implemented
        # HAS_KEY  # TODO: Add when implemented
    }

    LOGICAL_AXIOM_TYPES = filter(lambda ax: ax.is_logical, AXIOM_TYPES)
    LOGICAL_AXIOMS_AND_DECLARATIONS_TYPES = \
        itertools.chain(LOGICAL_AXIOM_TYPES, [DECLARATION])
    TBoxAxiomTypes = {
        SUBCLASS_OF, EQUIVALENT_CLASSES, DISJOINT_CLASSES,
        OBJECT_PROPERTY_DOMAIN,
        # OBJECT_PROPERTY_RANGE,  # TODO: Add when implemented
        # FUNCTIONAL_OBJECT_PROPERTY,  # TODO: Add when implemented
        # INVERSE_FUNCTIONAL_OBJECT_PROPERTY,  # TODO: Add when implemented
        DATA_PROPERTY_DOMAIN, DATA_PROPERTY_RANGE,
        # FUNCTIONAL_DATA_PROPERTY,  # TODO: Add when implemented
        # DATATYPE_DEFINITION,  # TODO: Add when implemented
        DISJOINT_UNION  # ,
        # HAS_KEY  # TODO: Add when implemented
    }
    ABoxAxiomTypes = {
        CLASS_ASSERTION,
        # SAME_INDIVIDUAL,  # TODO: Add when implemented
        DIFFERENT_INDIVIDUALS  # ,
        # OBJECT_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # NEGATIVE_OBJECT_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # DATA_PROPERTY_ASSERTION,  # TODO: Add when implemented
        # NEGATIVE_DATA_PROPERTY_ASSERTION  # TODO: Add when implemented
    }
    RBoxAxiomTypes = {
        # TRANSITIVE_OBJECT_PROPERTY,  # TODO: Add when implemented
        # DISJOINT_DATA_PROPERTIES,  # TODO: Add when implemented
        # SUB_DATA_PROPERTY,  # TODO: Add when implemented
        # EQUIVALENT_DATA_PROPERTIES,  # TODO: Add when implemented
        # DISJOINT_OBJECT_PROPERTIES,  # TODO: Add when implemented
        SUB_OBJECT_PROPERTY,
        # EQUIVALENT_OBJECT_PROPERTIES,  # TODO: Add when implemented
        # SUB_PROPERTY_CHAIN_OF,  # TODO: Add when implemented
        INVERSE_OBJECT_PROPERTIES  # ,
        # SYMMETRIC_OBJECT_PROPERTY,  # TODO: Add when implemented
        # ASYMMETRIC_OBJECT_PROPERTY,  # TODO: Add when implemented
        # REFLEXIVE_OBJECT_PROPERTY,  # TODO: Add when implemented
        # IRREFLEXIVE_OBJECT_PROPERTY  # TODO: Add when implemented
    }
    TBoxAndRBoxAxiomTypes = TBoxAxiomTypes.union(RBoxAxiomTypes)
    NAME_TYPE_MAP = {e: e.name for e in AXIOM_TYPES}
    CLASS_TYPE_MAP = {e: e.actual_class for e in AXIOM_TYPES}

    def __init__(
            self, actual_class, index, name, is_owl2_axiom,
            is_non_syntactic_owl2_axiom, is_logical):
        """
        :param actual_class: a class
        :param index: An integer object
        :param name: A string
        :param is_owl2_axiom: A Boolean
        :param is_non_syntactic_owl2_axiom: A Boolean
        :param is_logical: A Boolean
        """
        self.actual_class = actual_class
        self.index = index
        self.name = name
        self.is_owl2_axiom = is_owl2_axiom
        self.is_non_syntactic_owl2_axiom = is_non_syntactic_owl2_axiom
        self.is_logical = is_logical

    def hash_code(self):
        return hash(self.name)

    def __eq__(self, other):
        if other is None:
            return False

        if self is other:
            return True

        if isinstance(other, AxiomType):
            return self.name == other.name

        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.index > other.index

    def __lt__(self, other):
        return self.index < other.index

    @classmethod
    def get_type_for_class(cls, type_cls):
        """
        :param type_cls: A class
        :return: An AxiomType object
        """
        axiom_type = cls.CLASS_TYPE_MAP.get(type_cls)
        if axiom_type is None:
            raise RuntimeError('No known axiom type for %s' % str(type_cls))

        return axiom_type

    def get_axioms_without_types(self, source_axioms, *axiom_types):
        """
        Gets the set of axioms from a source set of axioms that are not of the
        specified type.

        TODO: Check the 'copy' semantics here

        :param source_axioms: The source set of axioms
        :param axiom_types: The types that will be filtered out of the source
        set
        :return: A set of axioms that represents the sourceAxioms without the
        specified types. Note that sourceAxioms will not be modified. The
        returned set is a copy.
        """
        disallowed = set(axiom_types)
        return filter(
            lambda ax: ax.get_axiom_type() not in disallowed,
            source_axioms)

    def get_axioms_of_type(self, source_axioms, *axiom_types):
        """
        Gets the set of axioms from a source set of axioms that have a
        specified type.

        TODO: Check the 'copy' semantics here

        :param source_axioms: The source set of axioms
        :param axiom_types: The types of axioms that will be returned
        :return: A set of axioms that represents the sourceAxioms that have
        the specified types. Note that sourceAxioms will not be modified. The
        returned set is a copy.
        """
        allowed = set(axiom_types)
        return filter(
            lambda ax: ax.get_axiom_type() in allowed,
            source_axioms)

    def get_axiom_type(self, name):
        return self.NAME_TYPE_MAP.get(name)

    def is_axiom_type(self, name):
        return name in self.NAME_TYPE_MAP
