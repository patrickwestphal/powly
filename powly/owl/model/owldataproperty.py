from rdflib.term import URIRef

from powly.owl.vocab.owlrdfvocabulary import OWLRDFVocabulary
from powly.owl.model.owldatapropertyexpression import OWLDataPropertyExpression
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlproperty import OWLProperty


class OWLDataProperty(OWLDataPropertyExpression, OWLProperty, OWLObject):
    def __init__(self, iri_or_str):
        super().__init__()
        assert iri_or_str is not None
        if isinstance(iri_or_str, str):
            self.iri = URIRef(iri_or_str)
        else:
            self.iri = iri_or_str
        self.built_in = \
            self.iri == OWLRDFVocabulary.OWL_TOP_DATA_PROPERTY.iri or \
            self.iri == OWLRDFVocabulary.OWL_BOTTOM_DATA_PROPERTY.iri

    def to_string_id(self):
        return str(self.iri)

    def is_built_in(self):
        return self.built_in

    def get_entity_type(self):
        raise NotImplementedError()

    def is_top_entity(self):
        return self.is_owl_top_data_property()

    def is_bottom_entity(self):
        return self.is_owl_bottom_data_property()

    def is_owl_top_data_property(self):
        return self.iri == OWLRDFVocabulary.OWL_TOP_DATA_PROPERTY.iri

    def is_owl_bottom_data_property(self):
        return self.iti == OWLRDFVocabulary.OWL_BOTTOM_DATA_PROPERTY

    @staticmethod
    def is_data_property_expression():
        return True

    @staticmethod
    def is_owl_data_property():
        return True

    def accept(self, visitor):
        raise NotImplementedError()

