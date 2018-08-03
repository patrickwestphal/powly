from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom
from powly.owl.model.owlsubpropertyaxiom import OWLSubPropertyAxiom


class OWLSubObjectPropertyOfAxiom(OWLSubPropertyAxiom, OWLObjectPropertyAxiom):
    def __init__(self, sub_property, super_property, annotations=None):
        """
        :param sub_property: An OWLObjectPropertyExpression object
        :param super_property: An OWLObjectPropertyExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

    def hash_index(self):
        return 127

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    @staticmethod
    def get_annotated_axiom(annotations):
        """
        :param annotations: A collection/generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()
