from powly.owl.model.owlliteralbase import OWLLiteralBase
from powly.owl.model.owlobject import OWLObject


class OWLLiteralBoolean(OWLLiteralBase, OWLObject):
    def __init__(self, literal):
        assert isinstance(literal, bool)
        self.literal = literal

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_datatype()))
        if self.literal:
            tmp_hsh = 65536
        else:
            tmp_hsh = 0
        hsh = OWLObject.hash_iteration(hsh, tmp_hsh)
        return OWLObject.hash_iteration(hsh, hash(self.get_lang()))

    def get_literal(self):
        return str(self.literal)

    def is_boolean(self):
        return True

    def parse_boolean(self):
        return self.literal

    def get_datatype(self):
        from powly.owl.util.internalizedentities import XSDBOOLEAN
        return XSDBOOLEAN
