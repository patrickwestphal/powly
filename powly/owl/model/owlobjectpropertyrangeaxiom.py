from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom
from powly.owl.model.owlpropertyrangeaxiom import OWLPropertyRangeAxiom


class OWLObjectPropertyRangeAxiom(OWLPropertyRangeAxiom, OWLObjectPropertyAxiom):
    """
    Represents
    <a href="http://www.w3.org/TR/owl2-syntax/#Object_Property_Range">ObjectPropertyRange</a>
    axioms in the OWL 2 specification.
    """

    def __init__(self, property, range, annotations=None):
        """
        :param property: An OWLObjectPropertyExpression objects
        :param range: An OWLClassExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, range, annotations)

    def hash_index(self):
        return 113

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A stream of OWLAnnotation objects
        :return:
        """
        raise NotImplementedError()

    def as_owl_sub_class_of_axiom(self):
        """
        TODO: Implement
        """
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.OBJECT_PROPERTY_RANGE
