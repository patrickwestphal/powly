from powly.owl.model.hasrange import HasRange
from powly.owl.model.owlsubclassofaxiomshortcut import OWLSubClassOfAxiomShortCut
from powly.owl.model.owlunarypropertyaxiom import OWLUnaryPropertyAxiom


class OWLPropertyRangeAxiom(
        OWLUnaryPropertyAxiom, OWLSubClassOfAxiomShortCut, HasRange):

    def __init__(self, property, range, annotations=None):
        """
        :param property: An OWLPropertyExpression object
        :param range: An OWLPropertyRange object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, annotations)
        assert range is not None
        self.range = range

    def get_range(self):
        return self.range

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()
