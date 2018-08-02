from rdflib.term import URIRef

from powly.owl.model.entitytype import EntityType
from powly.owl.model.owlobject import OWLObject
from powly.owl.vocab.owl2datatype import OWL2Datatype
from powly.owl.vocab.owlrdfvocabulary import OWLRDFVocabulary
from powly.owl.model.owldatarange import OWLDataRange
from powly.owl.model.owllogicalentity import OWLLogicalEntity
from powly.owl.model.owlnamedobject import OWLNamedObject


class OWLDatatype(OWLDataRange, OWLObject, OWLLogicalEntity, OWLNamedObject):
    def __init__(self, iri_or_string):
        """
        :param iri: An URIRef object or string
        """
        assert iri_or_string is not None
        if isinstance(iri_or_string, str):
            self.iri = URIRef(iri_or_string)
        else:
            self.iri = iri_or_string

        self.top = self.iri == OWLRDFVocabulary.RDFS_LITERAL.iri
        self.builtin = self.top or OWL2Datatype.is_built_in(self.iri) or \
            self.iri == OWLRDFVocabulary.RDF_PLAIN_LITERAL.iri

    def is_top_entity(self):
        return self.top

    @staticmethod
    def get_entity_type():
        return EntityType.DATATYPE

    def get_data_range_type(self):
        raise NotImplementedError()

    def is_string(self):
        """
        Determines if this datatype has the IRI xsd:string.
        :return:
        """
        return self.iri == OWL2Datatype.XSD_STRING.iri

    def is_integer(self):
        """
        Determines if this datatype has the IRI xsd:integer.
        """
        return self.iri == OWL2Datatype.XSD_INTEGER.iri

    def is_float(self):
        """
        Determines if this datatype has the IRI xsd:float.
        """
        return self.iri == OWL2Datatype.XSD_FLOAT.iri

    def is_double(self):
        """
        Determines if this datatype has the IRI xsd:double.
        """
        return self.iri == OWL2Datatype.XSD_DOUBLE.iri

    def is_boolean(self):
        """
        Determines if this datatype has the IRI xsd:boolean.
        """
        return self.iri == OWL2Datatype.XSD_BOOLEAN.iri

    def is_rdf_plain_literal(self):
        """
        Determines if this datatype has the IRI rdf:PlainLiteral.
        """
        raise NotImplementedError()

    def is_built_in(self):
        return self.builtin

    def get_built_in_datatype(self):
        """
        Gets the built in datatype information if this datatype is a built in
        datatype. This method should only be called if the isBuiltIn() method
        returns True

        :return: An OWL2Datatype object that describes this built in datatype
        """
        if self.builtin:
            return OWL2Datatype.get_datatype(self.iri)
        else:
            raise RuntimeError(
                '%s is not a built in datatype. The get_built_in_datatype() '
                'method should only be called on built in datatypes.' %
                str(self.iri))

    def accept(self):
        raise NotImplementedError()

    def to_string_id(self):
        return str(self.iri)

    def is_top_datatype(self):
        return self.top

    @staticmethod
    def is_owl_datatype():
        return True

    def get_iri(self):
        return self.iri
