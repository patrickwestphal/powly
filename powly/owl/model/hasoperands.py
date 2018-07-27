from abc import abstractmethod, ABC


class HasOperands(ABC):
    """An interface to objects that have a collection of operands."""

    @abstractmethod
    def operands(self):
        """
        Gets the operands - e.g., the individuals in a sameAs axiom, or the
        classes in an equivalent classes axiom.

        :return: A stream of operands
        """
        pass

    def get_operands_as_list(self):
        raise NotImplementedError()
