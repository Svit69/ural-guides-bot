class PaymentGatewayError(RuntimeError):
    """Raised when the payment provider cannot process a request."""

    def __init__(self, message: str, public_reason: str = "") -> None:
        super().__init__(message)
        self.public_reason = public_reason
