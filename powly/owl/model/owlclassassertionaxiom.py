from powly.owl.model.owlindividualaxiom import OWLIndividualAxiom
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlsubclassofaxiomshortcut import OWLSubClassOfAxiomShortCut


class OWLClassAssertionAxiom(OWLIndividualAxiom, OWLSubClassOfAxiomShortCut):
    def __init__(self, individual, class_expression, annotations=[]):
        super().__init__(annotations)
        assert individual is not None
        self.individual = individual
        assert class_expression is not None
        self.class_expression = class_expression

    def hash_index(self):
        return 7

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.individual))
        hsh = OWLObject.hash_iteration(hsh, hash(self.class_expression))
        return OWLObject.hash_iteration(hsh, hash(self.annotations))

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def getAnnotatedAxiom(self, annotations):
        """
        :param annotations: A collection/generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def get_individual(self):
        """
        Gets the individual that is asserted to be an instance of a class
        expression by this axiom.

        :return: An OWLIndividual object
        """
        return self.individual

    def get_class_expression(self):
        """
        Gets the class expression that is asserted to be a type for an
        individual by this axiom.

        :return: An OWLClassExpression object
        """
        return self.class_expression

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()

    def as_owl_sub_class_of_axiom(self):
        raise NotImplementedError()
