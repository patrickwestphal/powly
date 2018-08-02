from unittest.case import TestCase

from owl.model.owlclass import OWLClass
from owl.model.owlnaryclassaxiom import OWLNaryClassAxiom
from owl.model.owlobjectproperty import OWLObjectProperty
from owl.model.owlobjectsomevaluesfrom import OWLObjectSomeValuesFrom


class TestOWLNaryClassAxiom(TestCase):
    """OWLNaryClassAxiom test cases"""
    def test_components(self):
        prefix = 'http://example.com#'
        ce1 = OWLClass(prefix + 'Cls2')
        prop1 = OWLObjectProperty(prefix + 'objProp1')
        cls1 = OWLClass(prefix + 'Cls1')
        ce2 = OWLObjectSomeValuesFrom(prop1, cls1)
        ann1 = OWLAnnotation
        ceAx = OWLNaryClassAxiom()