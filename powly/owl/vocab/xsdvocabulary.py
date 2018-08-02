from enum import Enum
from rdflib.term import URIRef

from powly.owl.vocab.namespaces import Namespaces


class XSDVocabulary(Enum):
    ANY_TYPE = "anyType"
    ANY_SIMPLE_TYPE = "anySimpleType"
    STRING = "string"
    INTEGER = "integer"
    LONG = "long"
    INT = "int"
    SHORT = "short"
    BYTE = "byte"
    DECIMAL = "decimal"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DOUBLE = "double"
    NON_POSITIVE_INTEGER = "nonPositiveInteger"
    NEGATIVE_INTEGER = "negativeInteger"
    NON_NEGATIVE_INTEGER= "nonNegativeInteger"
    UNSIGNED_LONG = "unsignedLong"
    UNSIGNED_INT = "unsignedInt"
    POSITIVE_INTEGER = "positiveInteger"
    BASE_64_BINARY = "base64Binary"
    NORMALIZED_STRING = "normalizedString"
    HEX_BINARY = "hexBinary"
    ANY_URI = "anyURI"
    Q_NAME = "QName"
    NOTATION = "NOTATION"
    TOKEN = "token"
    LANGUAGE = "language"
    NAME = "Name"
    NCNAME = "NCName"
    NMTOKEN = "NMTOKEN"
    NMTOKENS = "NMTOKENS"
    ID = "ID"
    IDREF = "IDREF"
    IDREFS = "IDREFS"
    ENTITY = "ENTITY"
    ENTITIES = "ENTITIES"
    DURATION = "duration"
    DATE_TIME = "dateTime"
    DATE_TIME_STAMP = "dateTimeStamp"
    TIME = "time"
    DATE = "date"
    G_YEAR_MONTH = "gYearMonth"
    G_YEAR = "gYear"
    G_MONTH_DAY = "gMonthYear"
    G_DAY = "gDay"
    G_MONTH = "gMonth"
    UNSIGNED_SHORT = "unsignedShort"
    UNSIGNED_BYTE = "unsignedByte"

    def __init__(self, name):
        self.short_name = name
        self.prefixed_name = Namespaces.XSD.get_prefix_name() + ':' + name
        self.iri = URIRef(str(Namespaces.XSD) + name)

    def parse_short_name(self, short_name):
        """
        Easy parse of short names of the kind "xsd:typename". Note that the
        match must be exact - uppercase or lowercase variants are not accepted.
        An exception will be thrown for non matching input.

        :param short_name: string of the form xsd:typename
        :return: the XSDVocabulary item matching xsd:typename, e.g., STRING for
        "xsd:string"
        """
        raise NotImplementedError()
