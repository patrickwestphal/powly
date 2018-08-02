from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlindividualaxiom import OWLIndividualAxiom
from powly.owl.model.owlnaryaxiom import OWLNaryAxiom
from powly.owl.model.owlsubclassofaxiomsetshortcut import \
    OWLSubClassOfAxiomSetShortCut


class OWLNaryIndividualAxiom(
        OWLIndividualAxiom, OWLNaryAxiom, OWLSubClassOfAxiomSetShortCut,
        HasOperands):

    def __init__(self, individuals, annotations=None):
        """
        :param individuals: A collection of OWLIndividual objects
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert individuals is not None
        self.individuals = individuals
        self.individuals.sort()

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def individuals(self):
        """
        :return: A generator of OWLIndividual objects
        """
        return (i for i in self.individuals)

    def operands(self):
        return self.individuals()

    def get_individuals_as_list(self):
        return list(self.individuals)

    def get_operands_as_list(self):
        return list(self.individuals)
