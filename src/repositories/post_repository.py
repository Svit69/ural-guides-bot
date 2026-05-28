from src.database.connection_factory import SqliteConnectionFactory


class PostRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def save_post(self, post_number: int, text: str, photo_file_id: str | None) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.execute(
                """
                insert into posts values (?, ?, ?)
                on conflict(post_number) do update set
                    text = excluded.text,
                    photo_file_id = excluded.photo_file_id
                """,
                (post_number, text, photo_file_id),
            )

    def get_post(self, post_number: int) -> dict[str, str] | None:
        with self.__connection_factory.open_connection() as connection:
            row = connection.execute(
                "select * from posts where post_number = ?",
                (post_number,),
            ).fetchone()
        return dict(row) if row else None
