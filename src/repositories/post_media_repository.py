from src.database.connection_factory import SqliteConnectionFactory


class PostMediaRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def replace_post_media(self, post_number: int, media_items: list[dict[str, str]]) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.execute("delete from post_media where post_number = ?", (post_number,))
            for index, item in enumerate(media_items):
                connection.execute(
                    """
                    insert into post_media values (?, ?, ?, ?)
                    """,
                    (post_number, index, item["media_type"], item["file_id"]),
                )

    def get_post_media(self, post_number: int) -> list[dict[str, str]]:
        with self.__connection_factory.open_connection() as connection:
            rows = connection.execute(
                "select * from post_media where post_number = ? order by position",
                (post_number,),
            ).fetchall()
        return [dict(row) for row in rows]
