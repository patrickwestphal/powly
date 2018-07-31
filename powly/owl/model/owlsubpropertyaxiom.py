from powly.owl.model.owlpropertyaxiom import OWLPropertyAxiom


class OWLSubPropertyAxiom(OWLPropertyAxiom):
    def __init__(self, sub_property, super_property, annotations=None):
        super().__init__(annotations)
        assert sub_property is not None
        self.sub_property = sub_property
        assert super_property is not None
        self.super_property = super_property

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_sub_property(self):
        return self.sub_property

    def get_super_property(self):
        return self.super_property
