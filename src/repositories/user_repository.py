from datetime import UTC, datetime

from aiogram.types import User

from src.database.connection_factory import SqliteConnectionFactory


class UserRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def save_registered_user(self, user: User) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.execute(
                """
                insert into users values (?, ?, ?, ?)
                on conflict(telegram_id) do update set
                    username = excluded.username,
                    full_name = excluded.full_name
                """,
                (user.id, user.username, user.full_name, self.__get_current_time()),
            )

    def get_all_registered_users(self) -> list[dict[str, str]]:
        with self.__connection_factory.open_connection() as connection:
            rows = connection.execute(
                "select * from users order by registered_at desc"
            ).fetchall()
        return [dict(row) for row in rows]

    def __get_current_time(self) -> str:
        return datetime.now(UTC).isoformat(timespec="seconds")
