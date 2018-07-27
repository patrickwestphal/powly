from abc import ABC


class HasAnnotations(ABC):
    def annotations(self, p=None):
        """
        TODO: Implement

        :param p: annotation property to filter on
        :return: a sorted stream of OWLAnnotations on this object. This will
        only include the annotations contained in this object, not the value of
        annotation assertion axioms in an ontology or in other ontologies. Use
        the EntitySearcher methods for that purpose.
        """
        raise NotImplementedError()

    def annotations_as_list(self):
        """
        TODO: Implement
        """
        raise NotImplementedError()
