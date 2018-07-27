from abc import abstractmethod, ABC

from model.asowlannotationproperty import AsOWLAnnotationProperty
from model.asowlclass import AsOWLClass
from model.asowldataproperty import AsOWLDataProperty
from model.asowldatatype import AsOWLDatatype
from model.asowlnamedindividual import AsOWLNamedIndividual
from model.asowlobjectproperty import AsOWLObjectProperty
from model.owlnamedobject import OWLNamedObject
from model.owlprimitive import OWLPrimitive
from vocab.owlrdfvocabulary import OWLRDFVocabulary


class OWLEntity(
        OWLNamedObject, OWLPrimitive, AsOWLClass, AsOWLDataProperty,
        AsOWLDatatype, AsOWLAnnotationProperty, AsOWLNamedIndividual,
        AsOWLObjectProperty, ABC):
    """
    Represents
    <a href="http://www.w3.org/TR/owl2-syntax/#Entities.2C_Literals.2C_and_Anonymous_Individuals">Entities</a>
    in the OWL 2 Specification.
    """

    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def get_entity_type(self):
        pass

    def is_type(self, entity_type):
        """
        TESTME

        :param entity_type: An EntityType object
        """
        return self.get_entity_type() == entity_type

    def is_built_in(self):
        """
        TESTME

        Determines if this entity is a built in entity. The entity is a built in
        entity if it is:
        - a class and the URI corresponds to owl:Thing or owl:Nothing
        - an object property and the URI corresponds to owl:topObjectProperty
          or owl:bottomObjectProperty
        - a data property and the URI corresponds to owl:topDataProperty or
          owl:bottomDataProperty</li>
        - a datatype and the IRI is rdfs:Literal or is in the OWL 2 datatype
          map or is rdf:PlainLiteral
        - an annotation property and the URI is in the set of built in
          annotation property URIs, i.e. one of:
          - rdfs:label
          - rdfs:comment
          - rdfs:seeAlso
          - rdfs:isDefinedBy
          - owl:deprecated
          - owl:priorVersion
          - owl:backwardCompatibleWith
          - owl:incompatibleWith

        :return: Boolean indicating whether this entity is a built in entity
        """
        return self.uri in OWLRDFVocabulary.built_in_ap_iris()

    @abstractmethod
    def to_string_id(self):
        """
        Returns a string representation that can be used as the ID of this
        entity. This is the toString representation of the IRI
        """
        pass

    @abstractmethod
    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLEntityVisitor; or one of these classes: OWLNamedObjectVisitor,
        OWLNamedObjectVisitorEx, OWLObjectVisitor, OWLObjectVisitorEx
        """
        pass
