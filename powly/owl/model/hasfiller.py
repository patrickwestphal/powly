from abc import ABC, abstractmethod


class HasFiller(ABC):
    """An interface to objects that have a filler."""

    @abstractmethod
    def get_filler(self):
        """
        Gets the filler for this restriction. In the case of an object
        restriction this will be an individual, in the case of a data
        restriction this will be a constant (data value). For quantified
        restriction this will be a class expression or a data range.
        """
        pass
