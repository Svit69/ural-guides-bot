from pathlib import Path

from src.database.city_payment_schema_initializer import CityPaymentSchemaInitializer
from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.repositories.city_access_repository import CityAccessRepository


def test_counts_and_lists_city_buyers(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    DatabaseSchemaInitializer(connections).initialize_schema()
    CityPaymentSchemaInitializer(connections).initialize_schema()
    repository = CityAccessRepository(connections)

    with connections.open_connection() as connection:
        connection.execute(
            "insert into users values (?, ?, ?, ?)",
            (1, "nast_bar", "Настя", "2026-06-20T12:00:00"),
        )
    repository.grant_access(1, "payment-city")

    buyers = repository.get_users_with_access()

    assert repository.count_users_with_access() == 1
    assert buyers[0]["telegram_id"] == 1
    assert buyers[0]["username"] == "nast_bar"
