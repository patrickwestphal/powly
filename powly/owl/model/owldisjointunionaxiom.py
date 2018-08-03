from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlclassaxiom import OWLClassAxiom
from powly.owl.model.owlequivalentclassesaxiom import OWLEquivalentClassesAxiom
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlobjectunionof import OWLObjectUnionOf


class OWLDisjointUnionAxiom(OWLClassAxiom, HasOperands):
    def __init__(self, owl_class, class_expressions, annotations=None):
        """
        :param owl_class: An OWLClass object
        :param class_expressions: A collection/stream of OWLClassExpression
        objects
        """
        super().__init__(annotations)
        assert owl_class is not None
        self.owl_class = owl_class
        assert class_expressions is not None
        self.class_expressions = list(class_expressions)
        self.class_expressions.sort()

    def hash_index(self):
        return 43

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_owl_class()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_operands_as_list()))
        return OWLObject.hash_iteration(
            hsh, hash(self.annotations_as_list()))

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A collection/stream of annotations
        """
        raise NotImplementedError()

    def get_owl_class(self):
        """
        Gets the class which is equivalent to the disjoint union.
        """
        return self.owl_class

    def class_expressions(self):
        """
        Gets the class expressions which are operands of the disjoint union.

        :return: Sorted stream containing the operands of the disjoint union,
        note that this *does not* include the OWLClass that is equivalent to
        the disjoint union.
        """
        return (ce for ce in self.class_expressions)

    def operands(self):
        return self.class_expressions

    def get_operands_as_list(self):
        return self.class_expressions

    def get_owl_equivalent_classes_axiom(self):
        """
        Gets the part of this axiom that corresponds to an EquivalentClasses
        axiom.
        :return: The equivalent classes axiom part of this axiom. This is
        essentially, EquivalentClasses(CE, CEUnion) where CEUnion is the union
        of the classes returned by the getClassExpressions() method and CE is
        the class returned by the getOWLClass() method.
        """
        return OWLEquivalentClassesAxiom([
            self.owl_class, OWLObjectUnionOf(self.class_expressions)])

    def get_owl_disjoint_classes_axiom(self):
        """
        Gets the part of this axiom that corresponds to an DisjointClasses
        axiom.

        :return: The disjoint classes axiom part of this axiom. This is
        essentially, DisjointClasses(CE1, ..., CEn) where CEi in (CE1, ..., CEn)
        is contained in the classes returned by the getClassExpressions()
        method.
        """
        return OWLDisjointUnionAxiom(self.class_expressions)

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.DISJOINT_UNION
