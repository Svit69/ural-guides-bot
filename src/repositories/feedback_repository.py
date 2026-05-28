from datetime import UTC, datetime

from src.database.connection_factory import SqliteConnectionFactory


class FeedbackRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def save_feedback(self, payload: dict[str, object]) -> None:
        media = payload.get("media") or {}
        with self.__connection_factory.open_connection() as connection:
            connection.execute(
                """
                insert into feedback values (null, ?, ?, ?, ?, ?, ?)
                """,
                (
                    payload.get("user_id"),
                    payload.get("full_name"),
                    payload.get("text"),
                    media.get("media_type"),
                    media.get("file_id"),
                    datetime.now(UTC).isoformat(timespec="seconds"),
                ),
            )

    def get_all_feedback(self) -> list[dict[str, object]]:
        with self.__connection_factory.open_connection() as connection:
            rows = connection.execute(
                "select * from feedback order by created_at desc"
            ).fetchall()
        return [dict(row) for row in rows]
