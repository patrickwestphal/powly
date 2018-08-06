import itertools
from abc import abstractmethod

from powly.owl.model.owlannotationaxiom import OWLAnnotationAxiom
from powly.owl.model.owlobject import OWLObject


class OWLSubAnnotationPropertyOfAxiom(OWLAnnotationAxiom):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Annotation_Subproperties" >SubAnnotationPropertyOf</a>
    axiom in the OWL 2 Specification.
    """

    def __init__(self, sub_property, super_property, annotations=None):
        """
        :param sub_property: An OWLAnnotationProperty object
        :param super_property: An OWLAnnotationProperty object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert sub_property is not None
        self.sub_property = sub_property
        assert super_property is not None
        self.super_property = super_property

    def hash_index(self):
        return 829

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_sub_property()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_super_property()))
        return OWLObject.hash_iteration(hsh, hash(self.annotations_as_list()))

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def get_axiom_without_annotations(self, axiom):
        raise NotImplementedError()

    def components(self):
        return itertools.chain(
            (sbp for sbp in [self.get_sub_property()]),
            (spp for spp in [self.get_super_property()]),
            (ann for ann in self.annotations_as_list())
        )

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_sub_property(self):
        return self.sub_property

    def get_super_property(self):
        return self.super_property

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.SUB_ANNOTATION_PROPERTY_OF
