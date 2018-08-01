from powly.owl.model.hasproperty import HasProperty
from powly.owl.model.owlpropertyaxiom import OWLPropertyAxiom


class OWLUnaryPropertyAxiom(OWLPropertyAxiom, HasProperty):
    def __init__(self, property, annotations=None):
        """
        :param property: An OWLPropertyExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert property is not None
        self.property = property

    def get_property(self):
        return self.property

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

