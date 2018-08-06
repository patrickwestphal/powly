import itertools
from abc import abstractmethod

from powly.owl.model.hasdomain import HasDomain
from powly.owl.model.hasproperty import HasProperty
from powly.owl.model.owlannotationaxiom import OWLAnnotationAxiom
from powly.owl.model.owlobject import OWLObject


class OWLAnnotationPropertyDomainAxiom(
        OWLAnnotationAxiom, HasProperty, HasDomain):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Annotation_Property_Domain">AnnotationPropertyDomain</a>
    axiom in the OWL 2 specification.
    """

    def __init__(self, property, domain, annotations=None):
        """
        :param property: An OWLAnnotationProperty object
        :param domain: An URIRef object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert property is not None
        self.property = property
        assert domain is not None
        self.domain = domain

    def hash_index(self):
        return 823

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_property()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_domain()))
        return OWLObject.hash_iteration(hsh, hash(self.annotations_as_list()))

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def get_annotated_axiom(self, annotations):
        raise NotImplementedError()

    def get_domain(self):
        return self.domain

    def get_property(self):
        return self.property

    def components(self):
        return itertools.chain(
            (p for p in [self.get_property()]),
            (d for d in [self.get_domain()]),
            (ann for ann in self.annotations_as_list())
        )

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.ANNOTATION_PROPERTY_DOMAIN
