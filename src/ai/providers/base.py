from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Common interface for every AI provider."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:
        """Generate a text response from the AI provider."""
        raise NotImplementedError
