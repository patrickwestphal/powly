from powly.owl.model.hasdomain import HasDomain
from powly.owl.model.owlsubclassofaxiomshortcut import OWLSubClassOfAxiomShortCut
from powly.owl.model.owlunarypropertyaxiom import OWLUnaryPropertyAxiom


class OWLPropertyDomainAxiom(
        OWLUnaryPropertyAxiom, OWLSubClassOfAxiomShortCut, HasDomain):
    def __init__(self, property, domain, annotations=None):
        """
        :param property: An OWLPropertyExpression object
        :param domain: An OWLClassExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, annotations)
        assert domain is not None
        self.domain = domain

    def get_domain(self):
        return self.domain

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()
