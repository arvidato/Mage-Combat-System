from abc import ABC, abstractmethod


class Prototype(ABC):
    """Prototype interface that allows cloning objects."""

    @abstractmethod
    def clone(self):
        raise NotImplementedError

