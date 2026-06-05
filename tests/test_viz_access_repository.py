from pathlib import Path

from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.database.viz_payment_schema_initializer import VizPaymentSchemaInitializer
from src.repositories.viz_access_repository import VizAccessRepository


def test_counts_and_lists_viz_buyers(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    DatabaseSchemaInitializer(connections).initialize_schema()
    VizPaymentSchemaInitializer(connections).initialize_schema()
    repository = VizAccessRepository(connections)

    with connections.open_connection() as connection:
        connection.execute(
            "insert into users values (?, ?, ?, ?)",
            (1, "nast_bar", "Настя", "2026-06-05T12:00:00"),
        )
    repository.grant_access(1, "payment-1")

    buyers = repository.get_users_with_access()

    assert repository.count_users_with_access() == 1
    assert buyers[0]["telegram_id"] == 1
    assert buyers[0]["username"] == "nast_bar"
