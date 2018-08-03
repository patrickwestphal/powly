from rdflib.term import URIRef

from powly.owl.model.entitytype import EntityType
from powly.owl.model.owlindividual import OWLIndividual
from powly.owl.model.owllogicalentity import OWLLogicalEntity


class OWLNamedIndividual(OWLIndividual, OWLLogicalEntity):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Named_Individuals">Named Individual</a>
    in the OWL 2 Specification.
    """

    def __init__(self, iri_or_str):
        super().__init__()
        assert iri_or_str is not None
        if isinstance(iri_or_str, str):
            self.iri = URIRef(iri_or_str)
        else:
            self.iri = iri_or_str

    def hash_index(self):
        return 311

    def type_index(self):
        return 1005

    def to_string_id(self):
        return str(self.iri)

    def get_iri(self):
        return self.iri

    @staticmethod
    def get_entity_type():
        return EntityType.NAMED_INDIVIDUAL

    @staticmethod
    def is_owl_named_individual():
        return True

    @staticmethod
    def as_owl_anonymous_individual():
        raise RuntimeError('Not an anonymous individual')

    @staticmethod
    def is_built_in():
        return False

    def accept(self):
        raise NotImplementedError()

    def get_iri(self):
        return self.iri
