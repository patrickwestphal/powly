import itertools

from powly.owl.model.owlnaryclassaxiom import OWLNaryClassAxiom
from powly.owl.model.owlsubclassofaxiom import OWLSubClassOfAxiom


class OWLEquivalentClassesAxiom(OWLNaryClassAxiom):
    def __init__(self, class_expressions, annotations=None):
        """
        :param class_expressions: A collection of OWLClassExpression objects
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(class_expressions, annotations)

    def hash_index(self):
        return 53

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A collection/generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def contains_named_equivalent_class(self):
        """
        Determines if this equivalent classes axiom contains at least one named
        class (excluding owl:Thing or owl:Nothing).

        :return: A Boolean determining whether the axiom contains at least one
        named class
        """
        for ce in self.class_expressions:
            if self.named(ce):
                return True
        return False

    def named_classes(self):
        """
        Gets the named classes (excluding owl:Thing and owl:Nothing) that are
        in this equivalent classes axiom.
        :return: A set of classes that represents the named classes that are
        specified to be equivalent to some other class (expression),
        excluding the built in classes owl:Thing and owl:Nothing
        """
        return filter(lambda ce: self.named(ce), self.class_expressions)

    @staticmethod
    def named(ce):
        """
        :param ce: An OWLClassExpression object
        :return: A Boolean indicating whether the input class expression is a
        named class
        """
        return not ce.is_anonymous() and not ce.is_owl_nothing() and \
            not ce.is_owl_thing()

    def     contains_owl_nothing(self):
        """
        Determines if this class axiom makes a class expression equivalent
        to nothing.
        """
        for ce in self.class_expressions:
            if ce.is_owl_nothing():
                return True
        return False

    def contains_owl_thing(self):
        """
        Determines if this class axiom makes a class expression equivalent to
        thing.
        """
        for ce in self.class_expressions:
            if ce.is_owl_thing():
                return True
        return False

    def as_pairwise_axioms(self):
        """
        :return: A collection of OWLEquivalentClassesAxiom objects
        """
        return map(
            lambda equiv_pair: OWLEquivalentClassesAxiom([
                equiv_pair[0], equiv_pair[1]]),
            itertools.combinations(self.class_expressions, r=2))

    def split_to_annotated_pairs(self):
        """
        :return: A collection of OWLEquivalentClassesAxiom objects
        """
        return map(
            lambda equiv_pair: OWLEquivalentClassesAxiom([
                equiv_pair[0], equiv_pair[1]], self.annotations),
            itertools.combinations(self.class_expressions, r=2))

    def accept(self, visior):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()

    def as_owl_sub_class_of_axioms(self):
        return map(
            lambda ce_pair: OWLSubClassOfAxiom(ce_pair[0], ce_pair[1]),
            itertools.combinations(self.class_expressions, r=2))
