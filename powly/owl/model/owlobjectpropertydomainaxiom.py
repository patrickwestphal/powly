from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom
from powly.owl.model.owlobjectsomevaluesfrom import OWLObjectSomeValuesFrom
from powly.owl.model.owlpropertydomainaxiom import OWLPropertyDomainAxiom
from powly.owl.model.owlsubclassofaxiom import OWLSubClassOfAxiom
from powly.owl.util.internalizedentities import OWL_THING


class OWLObjectPropertyDomainAxiom(
        OWLPropertyDomainAxiom, OWLObjectPropertyAxiom):
    """
    Represents
    <a href="http://www.w3.org/TR/owl2-syntax/#Object_Property_Domain">ObjectPropertyDomain</a>
    axioms in the OWL 2 specification.
    """
    def __init__(self, property, domain, annotations=None):
        """
        :param property: An OWLObjectPropertyExpression object
        :param domain: An OWLClassExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(property, domain, annotations)

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A stream of OWLAnnotation objects
        """
        raise NotImplementedError()

    def as_owl_sub_class_of_axiom(self):
        sub = OWLObjectSomeValuesFrom(property, OWL_THING)
        return OWLSubClassOfAxiom(sub, self.domain)

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.OBJECT_PROPERTY_DOMAIN
