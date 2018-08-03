import itertools

from powly.owl.model.owlnaryclassaxiom import OWLNaryClassAxiom


class OWLDisjointClassesAxiom(OWLNaryClassAxiom):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Disjoint_Classes">DisjointClasses</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, class_expressions, annotations=None):
        """
        :param class_expressions: A collection of OWLClassExpression objcets
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(class_expressions, annotations)

    def hash_index(self):
        return 31

    def get_axiom_without_annotations(self):
        """
        :return: An OWLDisjointClassesAxiom objects
        """
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        TODO: do actual merge of annotations

        :param annotations: A stream of OWLAnnotation objects
        """
        return OWLDisjointClassesAxiom(
            self.class_expressions, self.annotations + annotations)

    def as_pairwise_axioms(self):
        """
        :return: A collection of OWLDisjointClassesAxiom objects
        """
        axioms = []
        for ce1, ce2 in itertools.combinations(self.class_expressions, r=2):
            axioms.append(OWLDisjointClassesAxiom([ce1, ce2]))

        return axioms

    def split_to_annotated_pairs(self):
        """
        :return: A collection of OWLDisjointClassesAxiom objects
        """
        raise NotImplementedError()

    def as_owl_sub_class_of_axioms(self):
        raise NotImplementedError()

    def accept(self, visitor):
        """TODO: Implement"""
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()
