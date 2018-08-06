from powly.owl.model.owldatapropertyaxiom import OWLDataPropertyAxiom
from powly.owl.model.owlsubpropertyaxiom import OWLSubPropertyAxiom


class OWLSubDataPropertyOfAxiom(OWLSubPropertyAxiom, OWLDataPropertyAxiom):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Data_Subproperties">SubDataPropertyOf</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, sub_property, super_property, annotations=None):
        """
        :param sub_property: An OWLDataPropertyExpression object
        :param super_property: An OWLDataPropertyExpression object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

    def hash_index(self):
        return 19

    def get_axiom_without_annotations(self, axiom):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.SUB_DATA_PROPERTY
