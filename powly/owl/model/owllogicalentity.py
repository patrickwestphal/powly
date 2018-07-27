from abc import abstractmethod, ABC

from model.owlentity import OWLEntity


class OWLLogicalEntity(OWLEntity, ABC):
    @abstractmethod
    def __init__(self, *args):
        pass
