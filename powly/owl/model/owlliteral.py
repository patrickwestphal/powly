from powly.owl.model.haslang import HasLang
from powly.owl.model.owlannotationvalue import OWLAnnotationValue
from powly.owl.model.owldatatype import OWLDatatype
from powly.owl.model.owlliteralbase import OWLLiteralBase
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlpropertyassertionobject import \
    OWLPropertyAssertionObject
from powly.owl.vocab.owl2datatype import OWL2Datatype


class OWLLiteral(
    OWLLiteralBase, OWLAnnotationValue, OWLPropertyAssertionObject, HasLang):

    RDF_PLAIN_LITERAL = OWLDatatype(OWL2Datatype.RDF_PLAIN_LITERAL)
    XSD_STRING = OWLDatatype(OWL2Datatype.XSD_STRING)
    RDF_LANG_STRING = OWLDatatype(OWL2Datatype.RDF_LANG_STRING)

    def __init__(self, literal, lang=None, datatype=None):
        assert literal is not None
        self.literal = literal

        if lang:
            self.lang = lang
            if datatype and \
                            datatype not in [self.XSD_STRING,
                                             self.RDF_LANG_STRING]:
                raise RuntimeError(
                    'Error: cannot build a literal with type: %s and '
                    'language: %s' % (datatype.iri, lang))
            self.datatype = self.RDF_LANG_STRING
        else:
            self.lang = ''
            if not datatype or datatype == self.RDF_PLAIN_LITERAL:
                self.datatype = self.XSD_STRING
            else:
                self.datatype = datatype

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_datatype()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_literal()) * 65536)
        return OWLObject.hash_iteration(hsh, hash(self.get_lang()))

    @staticmethod
    def as_boolean(string):
        return (string is not None and string.lower() == 'true') or \
               string.strip() == '1'

    def is_rdf_plain_literal(self):
        """
        Determines if the datatype of this literal is rdf:PlainLiteral. Note
        that literals that are abbreviated in the functional syntax (and other
        concrete syntaxes) and are of the form "abc" or "abc"@langTag will be
        of the type rdf:PlainLiteral after parsing.
        """
        return self.get_datatype().is_rdf_plain_literal()

    def get_literal(self):
        """
        Gets the lexical value of this literal. Note that if the datatype is
        rdf:PlainLiteral then the abbreviated lexical form will be returned.
        That is, the language tag is not included.
        """
        return self.literal

    def get_lang(self):
        return self.lang

    def get_datatype(self):
        """
        Gets the OWLDatatype which types this literal.
        """
        return self.datatype

    def has_lang(self, lang=None):
        """
        Determines if this literal has a particular language tag or a language
        tag at all, in case lang is None

        :param lang: A string of the specific lang to test for
        """
        if lang:
            # Comparison with input language
            return self.lang.lower() == lang.lower()
        elif self.lang:
            # No comparison; just checked whether self.lang is set
            return True
        else:
            return False

    def is_integer(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#integer.
        """
        return self.datatype.is_integer()

    def parse_integer(self):
        """
        Parses the lexical value of this literal into an integer. The lexical
        value of this literal should be in the lexical space of the integer
        datatype (http://www.w3.org/2001/XMLSchema#integer)
        """
        return int(self.get_literal())

    def is_boolean(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#boolean
        """
        return self.datatype().is_boolean()

    def parse_boolean(self):
        """
        Parses the lexical value of this literal into a boolean. The lexical
        value of this literal should be in the lexical space of the boolean
        datatype (http://www.w3.org/2001/XMLSchema#boolean).
        """
        return self.as_boolean(self.literal)

    def is_double(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#double.
        """
        return self.get_datatype().is_double()

    def parse_double(self):
        """
        Parses the lexical value of this literal into a double. The lexical
        value of this literal should be in the lexical space of the double
        datatype (http://www.w3.org/2001/XMLSchema#double).
        """
        return float(self.literal)

    def is_float(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#float.
        """
        return self.get_datatype().is_float()

    def parse_float(self):
        """
        Parses the lexical value of this literal into a float. The lexical
        value of this literal should be in the lexical space of the float
        datatype (http://www.w3.org/2001/XMLSchema#float).
        """
        return float(self.literal)
