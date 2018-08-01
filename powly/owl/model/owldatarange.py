from abc import abstractmethod

from powly.owl.model.asowldatatype import AsOWLDatatype
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlpropertyrange import OWLPropertyRange
from powly.owl.model.swrlpredicate import SWRLPredicate


class OWLDataRange(OWLObject, OWLPropertyRange, SWRLPredicate, AsOWLDatatype):
    @staticmethod
    def is_top_datatype():
        """
        Determines if this data range is the top data type.

        :return: Boolean indicating whether this data range is the top datatype
        """
        return False

    @abstractmethod
    def get_data_range_type(self):
        """
        Gets the type of this data range.

        :return: A DataRangeType object
        """
        pass

    def accept(self):
        raise NotImplementedError()
