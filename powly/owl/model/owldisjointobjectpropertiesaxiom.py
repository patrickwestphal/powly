import itertools

from powly.owl.model.owlnarypropertyaxiom import OWLNaryPropertyAxiom
from powly.owl.model.owlobjectpropertyaxiom import OWLObjectPropertyAxiom


class OWLDisjointObjectPropertiesAxiom(OWLNaryPropertyAxiom, OWLObjectPropertyAxiom):
    """
    Represents
    <a href="http://www.w3.org/TR/owl2-syntax/#Disjoint_Object_Properties" >DisjointObjectProperties</a>
    axioms in the OWL 2 specification.
    """
    def __init__(self, properties, annotations=None):
        """
        :param properties: A collection of OWLObjectPropertyExpression objects
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(properties, annotations)

    def hash_index(self):
        return 41

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        raise NotImplementedError()

    def as_pairwise_axioms(self):
        return [OWLDisjointObjectPropertiesAxiom([p1, p2])
                for p1, p2 in itertools.combinations(self.properties, r=2)]

    def split_to_annotated_pairs(self):
        return [OWLDisjointObjectPropertiesAxiom([p1, p2], self.annotations)
                for p1, p2 in itertools.combinations(self.properties, r=2)]

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.DISJOINT_OBJECT_PROPERTIES
