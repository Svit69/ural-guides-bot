from datetime import datetime, timezone

from src.database.connection_factory import SqliteConnectionFactory


class VizAccessRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def has_access(self, user_id: int) -> bool:
        with self.__connections.open_connection() as connection:
            row = connection.execute(
                "select 1 from viz_access where user_id = ?", (user_id,)
            ).fetchone()
        return row is not None

    def grant_access(self, user_id: int, payment_id: str) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                """
                insert or ignore into viz_access(user_id, payment_id, granted_at)
                values (?, ?, ?)
                """,
                (user_id, payment_id, datetime.now(timezone.utc).isoformat()),
            )

    def count_users_with_access(self) -> int:
        with self.__connections.open_connection() as connection:
            row = connection.execute("select count(*) as count from viz_access").fetchone()
        return int(row["count"])

    def get_users_with_access(self) -> list[dict[str, str]]:
        with self.__connections.open_connection() as connection:
            rows = connection.execute(
                """
                select a.user_id as telegram_id, u.username, u.full_name, a.granted_at
                from viz_access a
                left join users u on u.telegram_id = a.user_id
                order by a.granted_at desc
                """
            ).fetchall()
        return [dict(row) for row in rows]
