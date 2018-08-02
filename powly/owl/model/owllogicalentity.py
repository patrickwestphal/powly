from abc import abstractmethod, ABC

from powly.owl.model.owlentity import OWLEntity


class OWLLogicalEntity(OWLEntity, ABC):
    @abstractmethod
    def __init__(self, *args):
        super().__init__(*args)

    def components(self):
        raise NotImplementedError()
