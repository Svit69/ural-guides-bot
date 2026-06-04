from pathlib import Path

from src.database.connection_factory import SqliteConnectionFactory
from src.database.viz_payment_schema_initializer import VizPaymentSchemaInitializer
from src.repositories.viz_access_repository import VizAccessRepository
from src.repositories.viz_payment_repository import VizPaymentRepository


def test_migrates_successful_payment_to_permanent_access(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    initializer = VizPaymentSchemaInitializer(connections)
    initializer.initialize_schema()
    VizPaymentRepository(connections).save_payment(
        1,
        {
            "payment_id": "payment-1",
            "status": "succeeded",
            "confirmation_url": "https://pay",
        },
    )

    initializer.initialize_schema()

    assert VizAccessRepository(connections).has_access(1) is True
