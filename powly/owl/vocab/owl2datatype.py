import re
from enum import Enum
from rdflib.term import URIRef

from powly.owl.vocab.owlfacet import OWLFacet
from powly.owl.vocab.xsdvocabulary import XSDVocabulary
from powly.owl.vocab.namespaces import Namespaces


ANY = r'.*'
NUMBER = r'(\\+|-)?([0-9]+)(\\s)*(/)(\\s)*([0-9]+)'
NO_LINES = r'([^\\r\\n\\t])*'
INTNUMBER = r'(\\+|-)?([0-9]+)'
INTNOSIGN = r'(\\+)?([0-9]+)'
NEGINT = r'-([0-9]+)'
DECNUMBER = r'(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)'
NONNEG = r'((\\+)?([0-9]+))|-(0+)'
NONPOS = r'-([0-9]+)|(\\+(0+))'
XSTRING = r'([^\\s])(\\s([^\\s])|([^\\s]))*'
XLANG = r'[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*'
NAME1 = \
    r'[A-Z]|_|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|[\\u00F8-\\u02FF]|' \
    r'[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|[\\u200C-\\u200D]|' \
    r'[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|[\\u3001-\\uD7FF]|' \
    r'[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]'
NAME2 = \
    r'[A-Z]|_|[a-z]|[\\u00C0-\\u00D6]|[\\u00D8-\\u00F6]|[\\u00F8-\\u02FF]|' \
    r'[\\u0370-\\u037D]|[\\u037F-\\u1FFF]|[\\u200C-\\u200D]|' \
    r'[\\u2070-\\u218F]|[\\u2C00-\\u2FEF]|[\\u3001-\\uD7FF]|' \
    r'[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]|\"-\"|\".\"|[0-9]|' \
    r'\\u00B7|[\\u0300-\\u036F]|[\\u203F-\\u2040]'
XDOUBLE = \
    r'(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)([Ee](\\+|-)?[0-9]+)?|' \
    r'(\\+|-)?INF|NaN'
TSTAMP = \
    r'-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])' \
    r'T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|' \
    r'(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))'
BOOL = r'true|false|1|0'
HEX = r'([0-9a-fA-F]{2})*'
B64 = \
    r'((([A-Za-z0-9+/] ?){4})*(([A-Za-z0-9+/] ?){3}[A-Za-z0-9+/]|' \
    r'([A-Za-z0-9+/] ?){2}[AEIMQUYcgkosw048] ?=|[A-Za-z0-9+/] ?[AQgw] ?= ?=))?'


class Category(Enum):
    CAT_NUMBER = (
        'Number', OWLFacet.MIN_INCLUSIVE, OWLFacet.MAX_INCLUSIVE,
        OWLFacet.MIN_EXCLUSIVE, OWLFacet.MAX_EXCLUSIVE)
    CAT_STRING_WITH_LANGUAGE_TAG = (
        'String with a language tag', OWLFacet.MIN_LENGTH,
        OWLFacet.MAX_LENGTH, OWLFacet.LENGTH, OWLFacet.PATTERN,
        OWLFacet.LANG_RANGE)
    CAT_STRING_WITHOUT_LANGUAGE_TAG = (
        'String without a language tag', OWLFacet.MIN_LENGTH,
        OWLFacet.MAX_LENGTH, OWLFacet.LENGTH, OWLFacet.PATTERN)
    CAT_BINARY = (
        'Binary data', OWLFacet.MIN_LENGTH, OWLFacet.MAX_LENGTH,
        OWLFacet.LENGTH)
    CAT_URI = (
        'URI', OWLFacet.MIN_LENGTH, OWLFacet.MAX_LENGTH, OWLFacet.PATTERN)
    CAT_TIME = (
        'Time instant', OWLFacet.MIN_INCLUSIVE, OWLFacet.MAX_INCLUSIVE,
        OWLFacet.MIN_EXCLUSIVE, OWLFacet.MAX_EXCLUSIVE)
    CAT_BOOLEAN = ('Boolean value')
    CAT_UNIVERSAL = ('Universal literal')

    def __init__(self, category_name, *facets):
        self.category_name = category_name
        self.facets = facets


class OWL2Datatype(Enum):
    RDF_XML_LITERAL = (
        Namespaces.RDF, 'XMLLiteral', Category.CAT_STRING_WITHOUT_LANGUAGE_TAG,
        False, ANY)
    RDFS_LITERAL = (
        Namespaces.RDFS, 'Literal', Category.CAT_UNIVERSAL, False, ANY)
    RDF_PLAIN_LITERAL = (
        Namespaces.RDF, 'PlainLiteral', Category.CAT_STRING_WITH_LANGUAGE_TAG,
        False, ANY)
    RDF_LANG_STRING = (
        Namespaces.RDF, 'langString', Category.CAT_STRING_WITHOUT_LANGUAGE_TAG,
        False, ANY)
    OWL_REAL = (Namespaces.OWL, 'real', Category.CAT_NUMBER, False, ANY)
    OWL_RATIONAL = (
        Namespaces.OWL, 'rational', Category.CAT_NUMBER, False, NUMBER)
    XSD_STRING = (
        Namespaces.XSD, XSDVocabulary.STRING.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, ANY)
    XSD_NORMALIZED_STRING = (
        Namespaces.XSD, XSDVocabulary.NORMALIZED_STRING.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, NO_LINES)
    XSD_TOKEN = (
        Namespaces.XSD, XSDVocabulary.TOKEN.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, XSTRING)
    XSD_LANGUAGE = (
        Namespaces.XSD, XSDVocabulary.LANGUAGE.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, True, XLANG)
    XSD_NAME = (
        Namespaces.XSD, XSDVocabulary.NAME.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False,
        ':|'+NAME1+'(:|'+NAME2+')*')
    XSD_NCNAME = (
        Namespaces.XSD, XSDVocabulary.NCNAME.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, NAME1+'('+NAME2+')*')
    XSD_NMTOKEN = (
        Namespaces.XSD, XSDVocabulary.NMTOKEN.short_name,
        Category.CAT_STRING_WITHOUT_LANGUAGE_TAG, False, ANY)
    XSD_DECIMAL = (
        Namespaces.XSD, XSDVocabulary.DECIMAL.short_name, Category.CAT_NUMBER,
        False, DECNUMBER)
    XSD_INTEGER = (
        Namespaces.XSD, XSDVocabulary.INTEGER.short_name, Category.CAT_NUMBER,
        False, INTNUMBER)
    XSD_NON_NEGATIVE_INTEGER = (
        Namespaces.XSD, XSDVocabulary.NON_NEGATIVE_INTEGER.short_name,
        Category.CAT_NUMBER, False, NONNEG)
    XSD_NON_POSITIVE_INTEGER = (
        Namespaces.XSD, XSDVocabulary.NON_POSITIVE_INTEGER.short_name,
        Category.CAT_NUMBER, False, NONPOS)
    XSD_POSITIVE_INTEGER = (
        Namespaces.XSD, XSDVocabulary.POSITIVE_INTEGER.short_name,
        Category.CAT_NUMBER, False, INTNOSIGN)
    XSD_NEGATIVE_INTEGER = (
        Namespaces.XSD, XSDVocabulary.NEGATIVE_INTEGER.short_name,
        Category.CAT_NUMBER, False, NEGINT)
    XSD_LONG = (
        Namespaces.XSD, XSDVocabulary.LONG.short_name, Category.CAT_NUMBER,
        True, INTNUMBER)
    XSD_INT = (
        Namespaces.XSD, XSDVocabulary.INT.short_name, Category.CAT_NUMBER,
        True, INTNUMBER)
    XSD_SHORT = (
        Namespaces.XSD, XSDVocabulary.SHORT.short_name, Category.CAT_NUMBER,
        True, INTNUMBER)
    XSD_BYTE = (
        Namespaces.XSD, XSDVocabulary.BYTE.short_name, Category.CAT_NUMBER,
        True, INTNUMBER)
    XSD_UNSIGNED_LONG = (
        Namespaces.XSD, XSDVocabulary.UNSIGNED_LONG.short_name,
        Category.CAT_NUMBER, True, INTNOSIGN)
    XSD_UNSIGNED_INT = (
        Namespaces.XSD, XSDVocabulary.UNSIGNED_INT.short_name,
        Category.CAT_NUMBER, True, INTNOSIGN)
    XSD_UNSIGNED_SHORT = (
        Namespaces.XSD, XSDVocabulary.UNSIGNED_SHORT.short_name,
        Category.CAT_NUMBER, True, INTNOSIGN)
    XSD_UNSIGNED_BYTE = (
        Namespaces.XSD, XSDVocabulary.UNSIGNED_BYTE.short_name,
        Category.CAT_NUMBER, True, INTNOSIGN)
    XSD_DOUBLE = (
        Namespaces.XSD, XSDVocabulary.DOUBLE.short_name, Category.CAT_NUMBER,
        True, XDOUBLE)
    XSD_FLOAT = (
        Namespaces.XSD, XSDVocabulary.FLOAT.short_name, Category.CAT_NUMBER,
        True, XDOUBLE)
    XSD_BOOLEAN = (
        Namespaces.XSD, XSDVocabulary.BOOLEAN.short_name, Category.CAT_BOOLEAN,
        True, BOOL)
    XSD_HEX_BINARY = (
        Namespaces.XSD, XSDVocabulary.HEX_BINARY.short_name,
        Category.CAT_BINARY, False, HEX)
    XSD_BASE_64_BINARY = (
        Namespaces.XSD, XSDVocabulary.BASE_64_BINARY.short_name,
        Category.CAT_BINARY, False, B64)
    XSD_ANY_URI = (
        Namespaces.XSD, XSDVocabulary.ANY_URI.short_name, Category.CAT_URI,
        False, ANY)
    XSD_DATE_TIME = (
        Namespaces.XSD, XSDVocabulary.DATE_TIME.short_name, Category.CAT_TIME,
        False, TSTAMP+'?')
    XSD_DATE_TIME_STAMP = (
        Namespaces.XSD, XSDVocabulary.DATE_TIME_STAMP.short_name,
        Category.CAT_TIME, False, TSTAMP)

    @classmethod
    def EL_DATATYPES(cls):
        return [
            cls.RDF_PLAIN_LITERAL, cls.RDF_XML_LITERAL, cls.RDFS_LITERAL,
            cls.OWL_RATIONAL, cls.OWL_REAL, cls.XSD_DECIMAL, cls.XSD_INTEGER,
            cls.XSD_NON_NEGATIVE_INTEGER, cls.XSD_STRING,
            cls.XSD_NORMALIZED_STRING, cls.XSD_TOKEN, cls.XSD_NAME,
            cls.XSD_NCNAME, cls.XSD_NMTOKEN, cls.XSD_HEX_BINARY,
            cls.XSD_BASE_64_BINARY, cls.XSD_ANY_URI, cls.XSD_DATE_TIME,
            cls.XSD_DATE_TIME_STAMP]

    @classmethod
    def RL_DATATYPES(cls):
        return [
            cls.RDF_PLAIN_LITERAL, cls.RDF_XML_LITERAL, cls.RDFS_LITERAL,
            cls.XSD_DECIMAL, cls.XSD_INTEGER, cls.XSD_NON_NEGATIVE_INTEGER,
            cls.XSD_NON_POSITIVE_INTEGER, cls.XSD_POSITIVE_INTEGER,
            cls.XSD_NEGATIVE_INTEGER, cls.XSD_LONG, cls.XSD_INT, cls.XSD_SHORT,
            cls.XSD_BYTE, cls.XSD_UNSIGNED_LONG, cls.XSD_UNSIGNED_BYTE,
            cls.XSD_FLOAT, cls.XSD_DOUBLE, cls.XSD_STRING,
            cls.XSD_NORMALIZED_STRING, cls.XSD_TOKEN, cls.XSD_LANGUAGE,
            cls.XSD_NAME, cls.XSD_NCNAME, cls.XSD_NMTOKEN, cls.XSD_BOOLEAN,
            cls.XSD_HEX_BINARY, cls.XSD_BASE_64_BINARY, cls.XSD_ANY_URI,
            cls.XSD_DATE_TIME, cls.XSD_DATE_TIME_STAMP]

    @classmethod
    def ALL_IRIS(cls):
        return [
            cls.RDF_XML_LITERAL, cls.RDFS_LITERAL, cls.RDF_PLAIN_LITERAL,
            cls.RDF_LANG_STRING, cls.OWL_REAL, cls.OWL_RATIONAL,
            cls.XSD_STRING, cls.XSD_NORMALIZED_STRING, cls.XSD_TOKEN,
            cls.XSD_LANGUAGE, cls.XSD_NAME, cls.XSD_NCNAME, cls.XSD_NMTOKEN,
            cls.XSD_DECIMAL, cls.XSD_INTEGER, cls.XSD_NON_NEGATIVE_INTEGER,
            cls.XSD_NON_POSITIVE_INTEGER, cls.XSD_POSITIVE_INTEGER,
            cls.XSD_NEGATIVE_INTEGER, cls.XSD_LONG, cls.XSD_INT, cls.XSD_SHORT,
            cls.XSD_BYTE, cls.XSD_UNSIGNED_LONG, cls.XSD_UNSIGNED_INT,
            cls.XSD_UNSIGNED_SHORT, cls.XSD_UNSIGNED_BYTE, cls.XSD_DOUBLE,
            cls.XSD_FLOAT, cls.XSD_BOOLEAN, cls.XSD_HEX_BINARY,
            cls.XSD_BASE_64_BINARY, cls.XSD_ANY_URI, cls.XSD_DATE_TIME,
            cls.XSD_DATE_TIME_STAMP]

    def __init__(self, namespace, short_form, category, finite, reg_ex):
        self.iri = URIRef(str(namespace) + short_form)
        self.short_form = short_form
        self.prefixed_name = namespace.get_prefix_name() + ':' + short_form
        self.category = category
        self.finite = finite
        self.reg_expression = reg_ex
        self.pattern = re.compile(reg_ex)

    @classmethod
    def is_built_in(cls, datatype_iri):
        return datatype_iri in cls.ALL_IRIS

    def get_datatype(self):
        raise NotImplementedError()

    # TODO: Finish!
