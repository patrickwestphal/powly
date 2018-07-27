from abc import ABC, abstractmethod


class HasComponents(ABC):
    """
    An interface for objects that have a set of components - this is useful for
    all those situations where a generic action has to be performed on all
    components of an object, such as hashcode and equals computations, or
    rendering in a syntax.
    """

    @abstractmethod
    def components(self):
        """
        The stream is ordered (by visit order) but not sorted. Implementations
        that override  components() must ensure the order is compatible with
        __eq__() and __hash__().
        """
        pass

    def components_annotations_first(self):
        """
        :return: components as a stream; for objects that can have annotations
        on them, annotation streams appear first. This is useful in renderers.
        The stream is ordered (by visit order) but not sorted. Implementations
        that override components() must ensure the order is compatible with
        __eq__() and __hash__()
        """
        return self.components()

    def components_without_annotations(self):
        """
        :return: components as a stream; for objects that can have annotations
        on them, these are skipped. This is useful for comparing axioms without
        taking annotations into account. Note: annotations on nested objects
        are not affected.
        The stream is ordered (by visit order) but not sorted. Implementations
        that override components() must ensure the order is compatible with
        __eq__() and __hash__().
        """
        return self.components()
