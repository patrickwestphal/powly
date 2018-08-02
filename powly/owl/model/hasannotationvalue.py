from abc import abstractmethod, ABC


class HasAnnotationValue(ABC):
    @abstractmethod
    def annotationValue(self):
        """
        :return: An OWLAnnotationValue object
        """
        pass

    def when(self, witness, predicate, consumer, runnable):
        raise NotImplementedError()

    # ...

    # TODO: finish
