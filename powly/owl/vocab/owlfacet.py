from enum import Enum
from rdflib.term import URIRef

from powly.owl.model.hasiri import HasIRI
from powly.owl.vocab.namespaces import Namespaces


class OWLFacet(Enum, HasIRI):
    LENGTH = (Namespaces.XSD, 'length', 'length')
    MIN_LENGTH = (Namespaces.XSD, 'minLength', 'minLength')
    MAX_LENGTH = (Namespaces.XSD, 'maxLength', 'maxLength')
    PATTERN = (Namespaces.XSD, 'pattern', 'pattern')
    MIN_INCLUSIVE = (Namespaces.XSD, 'minInclusive', '>=')
    MIN_EXCLUSIVE = (Namespaces.XSD, 'minExclusive', '>')
    MAX_INCLUSIVE = (Namespaces.XSD, 'maxInclusive', '<=')
    MAX_EXCLUSIVE = (Namespaces.XSD, 'maxExclusive', '<')
    TOTAL_DIGITS = (Namespaces.XSD, 'totalDigits', 'totalDigits')
    FRACTION_DIGITS = (Namespaces.XSD, 'fractionDigits', 'fractionDigits')
    LANG_RANGE = (Namespaces.RDF, 'langRange', 'langRange')

    def __init__(self, ns, short_form, symbolic_form):
        self.iri = URIRef(str(ns) + short_form)
        self.short_form = short_form
        self.symbolic_form = symbolic_form
        self.prefixed_name = ns.get_prefix_name() + ':' + short_form

    def get_iri(self):
        return self.iri
