from abc import abstractmethod

from powly.owl.model.owlaxiom import OWLAxiom
from powly.owl.model.owlobject import OWLObject


class OWLDeclarationAxiom(OWLAxiom):

    def hash_index(self):
        return 23

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_entity()))
        return OWLObject.hash_iteration(hsh, hash(self.annotations_as_list()))

    @abstractmethod
    def get_axiom_without_annotations(self):
        pass

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    @abstractmethod
    def get_entity(self):
        pass

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()
