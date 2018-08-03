from powly.owl.model.axiomtype import AxiomType
from powly.owl.model.owlnarypropertyaxiom import OWLNaryPropertyAxiom
from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom


class OWLInverseObjectPropertiesAxiom(OWLNaryPropertyAxiom, OWLObjectPropertyAxiom):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Inverse_Object_Properties_2" >InverseObjectProperties</a>
    axiom in the OWL 2 Specification.

    Represents a statement that two properties are the inverse of each other.
    This property axiom contains a set of two properties. inverseOf(P, Q) is
    considered to be equal to inverseOf(Q, P) - i.e. the order in which the
    properties are specified isn't important.
    """

    def __init__(self, first, second, annotations=None):
        props = [first, second]
        props.sort()
        super().__init__(props, annotations)

        self.first = first
        self.second = second

    def hash_index(self):
        return 83

    def get_axiom_without_annotations(self, axiom):
        raise NotImplementedError()

    def as_pairwise_axioms(self):
        """
        :return: A collection of OWLInverseObjectPropertiesAxiom objects
        """
        return set(self)

    def split_to_annotated_pairs(self):
        """
        :return: A collection of OWLInverseObjectPropertiesAxiom objects
        """
        return self.as_pairwise_axioms()

    def get_first_property(self):
        """
        :return: An OWLObjectPropertyExpression
        """
        return self.first

    def get_second_property(self):
        """
        :return: An OWLObjectPropertyExpression
        """
        return self.second

    def as_sub_object_property_of_axioms(self):
        """
        TODO: Implement

        :return: A collection of OWLSubObjectPropertyOfAxiom objects
        """
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        """
        TODO: Check if semantic is correct here w.r.t. duplicates

        :param annotations: A collection of OWLAnnotation objects
        """
        return OWLInverseObjectPropertiesAxiom(
            self.first, self.second, self.annotations + annotations)

    def accept(self, visitor):
        """TODO: Implement"""
        raise NotImplementedError()

    def get_axiom_type(self):
        return AxiomType.INVERSE_OBJECT_PROPERTIES
