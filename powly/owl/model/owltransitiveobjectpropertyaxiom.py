from abc import abstractmethod

from powly.owl.model.owlobjectpropertycharacteristicaxiom import \
    OWLObjectPropertyCharacteristicAxiom


class OWLTransitiveObjectPropertyAxiom(OWLObjectPropertyCharacteristicAxiom):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Transitive_Object_Properties">TransitiveObjectProperty</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, property, annotations=None):
        """
        :param property: An OWLObjectPropertyExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, annotations)

    def hash_index(self):
        return 151

    def get_axiom_without_annotations(self, axiom):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.TRANSITIVE_OBJECT_PROPERTY
