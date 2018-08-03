from powly.owl.model.owldatapropertyaxiom import OWLDataPropertyAxiom
from powly.owl.model.owlpropertyrangeaxiom import OWLPropertyRangeAxiom


class OWLDataPropertyRangeAxiom(OWLPropertyRangeAxiom, OWLDataPropertyAxiom):
    def __init__(self, property, range, annotations=None):
        """
        :param property: An OWLDataPropertyExpression objects
        :param range: An OWLDataRange expression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, range, annotations)

    def hash_index(self):
        return 17

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A collection/generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def as_owl_sub_class_of_axiom(self):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()
