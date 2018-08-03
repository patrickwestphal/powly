from powly.owl.model.owldatapropertyaxiom import OWLDataPropertyAxiom
from powly.owl.model.owlpropertydomainaxiom import OWLPropertyDomainAxiom


class OWLDataPropertyDomainAxiom(OWLPropertyDomainAxiom, OWLDataPropertyAxiom):
    def __init__(self, property, domain, annotations=None):
        """
        :param property: An OWLDataPropertyExpression object
        :param domain: An OWLClassExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, domain, annotations)

    def hash_index(self):
        return 13

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A collection of OWLAnnotation objects
        """
        raise NotImplementedError()

    def as_owl_sub_class_of_axiom(self):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        raise NotImplementedError()
