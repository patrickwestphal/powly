from abc import abstractmethod, ABC


class OWLVisitorBase(ABC):
    """
    Base interface for visitors.
    """
    @abstractmethod
    def do_default(self, obj):
        """
        Default action for the visitor.
        """
        pass
