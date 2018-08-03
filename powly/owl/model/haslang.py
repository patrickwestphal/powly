from abc import ABC, abstractmethod


class HasLang(ABC):
    @abstractmethod
    def get_lang(self):
        """
        Gets the language tag of the literal.

        :return: A string representing the language tag of a literal. If the
        literal does not have a language tag, because it is not of the type
        rdf:PlainLiteral, or because its language tag is empty, then the empty
        string will be returned.
        """
        pass
