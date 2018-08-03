from abc import abstractmethod, ABC

from powly.owl.model.owlentity import OWLEntity
from powly.owl.model.owlobject import OWLObject


class OWLLogicalEntity(OWLEntity, ABC):
    @abstractmethod
    def __init__(self, *args):
        super().__init__(*args)

    def __hash__(self):
        return OWLObject.hash_iteration(self.hash_index(), hash(self.get_iri()))

    def components(self):
        return (i for i in self.get_iri())
