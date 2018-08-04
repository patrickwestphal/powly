import itertools
from abc import abstractmethod, ABC

from powly.owl.model.hasfiller import HasFiller
from powly.owl.model.owlanonymousclassexpression import \
    OWLAnonymousClassExpression
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlrestriction import OWLRestriction


class OWLHasValueRestriction(
        OWLRestriction, OWLAnonymousClassExpression, HasFiller, ABC):

    @abstractmethod
    def __init__(self, value):
        """
        :param value: An OWLObject object
        """
        super().__init__()
        self.value = value

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_property))
        return OWLObject.hash_iteration(hsh, hash(self.get_filler()))

    def get_filler(self):
        return self.value

    def get_value(self):
        return self.get_filler()

    def components(self):
        return itertools.chain(
            (p for p in [self.get_property()]),
            (f for f in [self.get_filler()])
        )

    @abstractmethod
    def as_some_values_from(self):
        """
        A convenience method that obtains this restriction as an existential
        restriction with a nominal filler.

        :return: The existential equivalent of this value restriction.
        simp(HasValue(p a)) = some(p {a})
        """
        pass
