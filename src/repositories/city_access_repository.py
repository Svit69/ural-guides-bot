from datetime import datetime, timezone

from src.database.connection_factory import SqliteConnectionFactory


class CityAccessRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def has_access(self, user_id: int) -> bool:
        with self.__connections.open_connection() as connection:
            row = connection.execute(
                "select 1 from city_access where user_id = ?", (user_id,)
            ).fetchone()
        return row is not None

    def grant_access(self, user_id: int, payment_id: str) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                "insert or ignore into city_access values (?, ?, ?)",
                (user_id, payment_id, datetime.now(timezone.utc).isoformat()),
            )
