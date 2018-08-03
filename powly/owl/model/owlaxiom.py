from abc import abstractmethod

from powly.owl.model.hasannotations import HasAnnotations
from powly.owl.model.owlobject import OWLObject


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

    def type_index(self):
        return 2000 + self.get_axiom_type().get_index()

    def annotations(self):
        return (ann for ann in self.annotations)

    def annotations_as_list(self):
        return self.annotations

    def get_axiom_without_annotations(self, axiom):
        """
        Gets an axiom that is structurally equivalent to the input axiom without
        annotations. This essentially returns a version of the axiom stripped of
        any annotations.
        :param axiom: OWLAxiom object to divest of annotations
        :return: The annotationless version of the imput axiom
        """
        # FIXME: axiom could be None, a class type, or an OWLAxiom!
        raise NotImplementedError()

    @staticmethod
    def get_annotated_axiom(annotations, axiom):
        # FIXME: Multiple implementations with differing method signature!!!
        return axiom.get_annotated_axiom(type(axiom), annotations)

    def is_anonymous(self):
        return True

    @staticmethod
    def is_individual():
        return False

    @staticmethod
    def is_axiom():
        return True

    def accept(self, visitor):
        raise NotImplementedError()

    def equals_ignore_annotations(self, axiom):
        """
        :param axiom: An OWLAxiom object
        """
        raise NotImplementedError()

    def is_logical_axiom(self):
        """
        Determines if this axiom is a logical axiom. Logical axioms are defined
        to be axioms other than both declaration axioms (including imports
        declarations) and annotation axioms.
        """
        return False

    def is_annotation_axiom(self):
        """
        Determines if this axioms in an annotation axiom (an instance of
        OWLAnnotationAxiom)
        """
        return False

    def is_annotated(self):
        """
        Determines if this axiom has any annotations on it
        """
        return len(self.annotations) != 0


    @abstractmethod
    def get_axiom_type(self):
        pass

    def is_of_type(self, types):
        if self.get_axiom_type() in types:
            return True
        else:
            return False

    def get_nnf(self):
        raise NotImplementedError()
