from powly.owl.model.owlclassaxiom import OWLClassAxiom


class OWLSubClassOfAxiom(OWLClassAxiom):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Subclass_Axioms">SubClassOf</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, sub_class, super_class, annotations=None):
        """
        :param sub_class: An OWLClassExpression object
        :param super_class: An OWLClassExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert sub_class is not None
        self.sub_class = sub_class

        assert super_class is not None
        self.super_class = super_class

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A collection/generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_sub_class(self):
        return self.sub_class

    def get_super_class(self):
        return self.super_class

    def is_gci(self):
        """
        Determines if this subclass axiom has a subclass that is anonymous.
        (if the subclass is anonymous then the subclass axiom is known as a
        General Concept Inclusion - GCI).

        :return: A Boolean indicating whether this axiom is a GCI
        """
        return self.sub_class.is_anonymous()

    def accept(self, visitor):
        raise NotImplementedError()
