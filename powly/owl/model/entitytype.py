from abc import ABC, abstractmethod
from enum import Enum

from vocab.owlrdfvocabulary import OWLRDFVocabulary


class Builder(ABC):
    @abstractmethod
    def build_entity(self, uri, provider):
        """
        :param uri: An URIRef object
        :param provider: An EntityProvider object
        """
        pass


class EntityType(Enum):
    CLASS = (
        'Class', 'Class', 'Classes', OWLRDFVocabulary.OWL_CLASS,
        lambda i, p: p.getOWLClass(i))
    OBJECT_PROPERTY = (
        'ObjectProperty', 'Object property', 'Object properties',
        OWLRDFVocabulary.OWL_OBJECT_PROPERTY,
        lambda i, p: p.getOWLObjectProperty(i))
    DATA_PROPERTY = (
        'DataProperty', 'Data property', 'Data properties',
        OWLRDFVocabulary.OWL_DATA_PROPERTY,
        lambda i, p: p.getOWLDataProperty(i))
    ANNOTATION_PROPERTY = (
        'AnnotationProperty', 'Annotation property', 'Annotation properties',
        OWLRDFVocabulary.OWL_ANNOTATION_PROPERTY,
        lambda i, p: p.getOWLAnnotationProperty(i))
    NAMED_INDIVIDUAL = (
        'NamedIndividual', 'Named individual', 'Named individuals',
        OWLRDFVocabulary.OWL_NAMED_INDIVIDUAL,
        lambda i, p: p.getOWLNamedIndividual(i))
    DATATYPE = (
        'Datatype', 'Datatype', 'Datatypes', OWLRDFVocabulary.RDFS_DATATYPE,
        lambda i, p: p.getOWLDatatype(i))

    def __init__(
            self, name, print_name, plural_print_name, vocabulary, builder):
        """
        :param name: A string
        :param print: A string
        :param plural_print_name: A string
        :param vocabulary: an OWLRDFVocabulary object
        :param builder: A Builder object
        """
        self.name_ = name
        self.print_name = print_name
        self.plural_print_name = plural_print_name
        self.vocabulary = vocabulary
        self.builder = builder

    def __str__(self):
        return self.name_

    def __repr__(self):
        return str(self)
