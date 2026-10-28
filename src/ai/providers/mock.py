from .base import AIProvider


class MockProvider(AIProvider):
    """Development provider that does not call an external AI."""

    def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:
        return "Mock AI response."
