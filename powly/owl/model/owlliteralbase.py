import itertools

from abc import ABC, abstractmethod

from powly.owl.model.owlobject import OWLObject


class OWLLiteralBase(ABC):
    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_datatype()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_literal()))
        return OWLObject.hash_iteration(hsh, hash(self.get_lang()))

    def components(self):
        return itertools.chain(
            self.get_datatype(), self.get_literal(), self.get_lang())

    def hash_index(self):
        return 277

    def type_index(self):
        return 4008

    @abstractmethod
    def is_rdf_plain_literal(self):
        """
        Determines if the datatype of this literal is rdf:PlainLiteral. Note
        that literals that are abbreviated in the functional syntax (and other
        concrete syntaxes) and are of the form "abc" or "abc"@langTag will be
        of the type rdf:PlainLiteral after parsing.
        """
        pass

    @abstractmethod
    def get_literal(self):
        """
        Gets the lexical value of this literal. Note that if the datatype is
        rdf:PlainLiteral then the abbreviated lexical form will be returned.
        That is, the language tag is not included.
        """
        pass

    def get_lang(self):
        return ''

    @abstractmethod
    def get_datatype(self):
        """
        Gets the OWLDatatype which types this literal.
        """
        pass

    def has_lang(self, lang=None):
        """
        Determines if this literal has a particular language tag or a language
        tag at all, in case lang is None

        :param lang: A string of the specific lang to test for
        """
        return False

    def is_integer(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#integer.
        """
        return False

    def parse_integer(self):
        """
        Parses the lexical value of this literal into an integer. The lexical
        value of this literal should be in the lexical space of the integer
        datatype (http://www.w3.org/2001/XMLSchema#integer)
        """
        raise RuntimeError(
            '%s does not have an int value but has %s' % (
                str(type(self)), self.get_literal()))

    def is_boolean(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#boolean
        """
        return False

    def parse_boolean(self):
        """
        Parses the lexical value of this literal into a boolean. The lexical
        value of this literal should be in the lexical space of the boolean
        datatype (http://www.w3.org/2001/XMLSchema#boolean).
        """
        raise RuntimeError(
            '%s does not have a boolean value but has %s' % (
                str(type(self)), self.get_literal()))

    def is_double(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#double.
        """
        return False

    def parse_double(self):
        """
        Parses the lexical value of this literal into a double. The lexical
        value of this literal should be in the lexical space of the double
        datatype (http://www.w3.org/2001/XMLSchema#double).
        """
        raise RuntimeError(
            '%s does not have a double value but has %s' % (
                str(type(self)), self.get_literal()))

    def is_float(self):
        """
        Determines if this literal is typed with a datatype that has an IRI
        that is http://www.w3.org/2001/XMLSchema#float.
        """
        return False

    def parse_float(self):
        """
        Parses the lexical value of this literal into a float. The lexical
        value of this literal should be in the lexical space of the float
        datatype (http://www.w3.org/2001/XMLSchema#float).
        """
        raise RuntimeError(
            '%s does not have a double value but has %s' % (
                str(type(self)), self.get_literal()))

    def is_literal(self):
        return True

    def as_literal(self):
        return self

    def accept(self, visitor):
        raise NotImplementedError()
