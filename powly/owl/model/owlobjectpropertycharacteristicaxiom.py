from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom
from powly.owl.model.owlunarypropertyaxiom import OWLUnaryPropertyAxiom


class OWLObjectPropertyCharacteristicAxiom(
        OWLObjectPropertyAxiom, OWLUnaryPropertyAxiom):

    def __init__(self, property, annotations=None):
        """
        :param property: An OWLObjectPropertyExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert property is not None
        self.property = property

    def get_property(self):
        return self.property
