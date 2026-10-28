from anthropic import Anthropic

from ..client import get_anthropic_api_key
from .base import AIProvider


class AnthropicProvider(AIProvider):
    """Anthropic Claude provider."""

    def __init__(self, model: str):
        self.model = model
        self.client = Anthropic(api_key=get_anthropic_api_key())

    def generate(
        self,
        prompt: str,
        system: str | None = None,
    ) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system or "",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text
