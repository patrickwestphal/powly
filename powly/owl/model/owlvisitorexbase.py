from abc import abstractmethod, ABC


class OWLVisitorExBase(ABC):
    """
    Base interface for visitors that return a value.
    """

    @abstractmethod
    def do_default(self, object):
        """
        Gets the default return value for this visitor.
        """
        pass
