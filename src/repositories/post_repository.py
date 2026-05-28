from src.database.connection_factory import SqliteConnectionFactory


class PostRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def save_post(self, post_number: int, text: str) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.execute(
                """
                insert into posts values (?, ?, null)
                on conflict(post_number) do update set
                    text = excluded.text
                """,
                (post_number, text),
            )

    def get_post(self, post_number: int) -> dict[str, str] | None:
        with self.__connection_factory.open_connection() as connection:
            row = connection.execute(
                "select * from posts where post_number = ?",
                (post_number,),
            ).fetchone()
        return dict(row) if row else None
