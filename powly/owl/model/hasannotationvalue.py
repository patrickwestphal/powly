from abc import abstractmethod, ABC


class HasAnnotationValue(ABC):
    @abstractmethod
    def annotation_value(self):
        """
        :return: An OWLAnnotationValue object
        """
        pass

    def when(self, witness, predicate, consumer, runnable):
        raise NotImplementedError()

    # ...

    # TODO: finish
