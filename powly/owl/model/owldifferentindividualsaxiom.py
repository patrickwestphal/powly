import itertools

from powly.owl.model.owlnaryindividualaxiom import OWLNaryIndividualAxiom
from powly.owl.model.owlobjectoneof import OWLObjectOneOf
from powly.owl.model.owlsubclassofaxiom import OWLSubClassOfAxiom


class OWLDifferentIndividualsAxiom(OWLNaryIndividualAxiom):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Individual_Inequality" >DifferentIndividuals</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, individuals, annotations=None):
        """
        :param individuals: A collection of OWLIndividual objects
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(individuals, annotations)

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def contains_anonymous_individuals(self):
        """
        Determines whether this axiom contains anonymous individuals. Anonymous
        individuals are not allowed in different individuals axioms.
        """
        for indiv in self.individuals:
            if indiv.is_anonymous():
                return True
        return False

    def as_pairwise_axioms(self):
        return map(
            lambda indiv_pair: OWLDifferentIndividualsAxiom([
                indiv_pair[0], indiv_pair[1]]),
            itertools.combinations(self.individuals, r=2))

    def split_to_annotated_pairs(self):
        return map(
            lambda indiv_pair: OWLDifferentIndividualsAxiom([
                indiv_pair[0], indiv_pair[1]], self.annotations),
            itertools.combinations(self.individuals, r=2))

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()

    def as_owl_sub_class_of_axioms(self):
        return map(
            lambda indiv_pair: OWLSubClassOfAxiom(
                OWLObjectOneOf([indiv_pair[0]]),
                OWLObjectOneOf([indiv_pair[1]]).get_object_complement_of()),
            itertools.combinations(self.individuals, r=2))
