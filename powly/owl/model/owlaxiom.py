from owl.model.hasannotations import HasAnnotations
from owl.model.owlobject import OWLObject


class OWLAxiom(OWLObject, HasAnnotations):
    """
    Represents <a href="http://www.w3.org/TR/owl2-syntax/#Axioms">Axioms</a> in
    the OWL 2 Specification.

    An OWL ontology contains a set of axioms. These axioms can be annotation
    axioms, declaration axioms, imports axioms or logical axioms
    """

    def __init__(self, annotations=None):
        super().__init__()

        if annotations is None:
            self.annotations = []
        else:
            self.annotations = annotations
        self.annotations.sort()

    @staticmethod
    def get_axiom_without_annotations(axiom):
        """
        Gets an axiom that is structurally equivalent to the input axiom without
        annotations. This essentially returns a version of the axiom stripped of
        any annotations.
        :param axiom: OWLAxiom object to divest of annotations
        :return: The annotationless version of the imput axiom
        """
        raise NotImplementedError()

    # ... TODO: Finish
