from .providers.base import AIProvider


class AIEngine:
    """Provider-independent AI engine."""

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:
        return self.provider.generate(
            prompt=prompt,
            system=system,
        )