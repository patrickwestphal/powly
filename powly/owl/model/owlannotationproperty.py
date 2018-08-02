from rdflib.term import URIRef

from powly.owl.model.entitytype import EntityType
from powly.owl.model.owlproperty import OWLProperty
from powly.owl.vocab.owlrdfvocabulary import OWLRDFVocabulary


class OWLAnnotationProperty(OWLProperty):
    def __init__(self, iri_or_string):
        super().__init__()
        if isinstance(iri_or_string, str):
            self.iri = URIRef(iri_or_string)
        else:
            self.iri = iri_or_string

    def to_string_id(self):
        return str(self.iri)

    def hash_index(self):
        return 857

    def type_index(self):
        return 1006

    def get_entity_type(self):
        return EntityType.ANNOTATION_PROPERTY

    def is_comment(self):
        """
        Determines if this annotation property has an IRI corresponding to
        rdfs:comment
        """
        return self.get_iri() == OWLRDFVocabulary.RDFS_COMMENT.get_iri()

    def is_label(self):
        """
        Determines if this annotation property has an IRI corresponding to
        rdfs:label.
        """
        return self.get_iri() == OWLRDFVocabulary.RDFS_LABEL.get_iri()

    def is_deprecated(self):
        """
        Determines if this annotation property has an IRI corresponding to
        owl:deprecated. An annotation along the owl:deprecated property which
        has a value of "true"^^xsd:boolean can be used to deprecate IRIs. (See
        <a href ="http://www.w3.org/TR/owl2-syntax/#Annotation_Properties">Section 5.5</a>
        of the OWL 2 specification.
        """
        return self.get_iri() == OWLRDFVocabulary.OWL_DEPRECATED.get_iri()

    def is_owl_annotation_property(self):
        return True

    def get_iri(self):
        return self.iri

    def accept(self, visitor):
        raise NotImplementedError()
