from src.database.connection_factory import SqliteConnectionFactory


class AdminRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def add_admin(self, telegram_id: int) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.execute(
                "insert or ignore into admins (telegram_id) values (?)",
                (telegram_id,),
            )

    def is_admin(self, telegram_id: int) -> bool:
        with self.__connection_factory.open_connection() as connection:
            row = connection.execute(
                "select 1 from admins where telegram_id = ?",
                (telegram_id,),
            ).fetchone()
        return row is not None
