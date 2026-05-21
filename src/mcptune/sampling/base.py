from abc import ABC, abstractmethod


class ArgumentSampler(ABC):

    @abstractmethod
    def sample(self, schema: dict) -> any:
        """
        Generate a valid value for a given JSONSchema fragment.
        """
        pass
