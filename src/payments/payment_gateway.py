from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    async def create_viz_payment(self, user_id: int) -> dict[str, str]:
        """Create a payment and return its provider data."""

    @abstractmethod
    async def create_city_payment(self, user_id: int) -> dict[str, str]:
        """Create a city guide payment and return its provider data."""

    @abstractmethod
    async def get_payment(self, payment_id: str) -> dict[str, object]:
        """Return current payment information from the provider."""
