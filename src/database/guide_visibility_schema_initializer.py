from src.database.connection_factory import SqliteConnectionFactory


class GuideVisibilitySchemaInitializer:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def initialize_schema(self) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                """
                create table if not exists guide_visibility (
                    guide_id text primary key,
                    is_visible integer not null
                )
                """
            )
            values = [("big_konny", 1), ("viz", 1), ("city_walk", 1), ("chekists", 0)]
            connection.executemany(
                "insert or ignore into guide_visibility values (?, ?)", values
            )
