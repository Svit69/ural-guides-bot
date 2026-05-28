from src.database.connection_factory import SqliteConnectionFactory


class DatabaseSchemaInitializer:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connection_factory = connection_factory

    def initialize_schema(self) -> None:
        with self.__connection_factory.open_connection() as connection:
            connection.executescript(
                """
                create table if not exists admins (
                    telegram_id integer primary key
                );
                create table if not exists users (
                    telegram_id integer primary key,
                    username text,
                    full_name text,
                    registered_at text not null
                );
                create table if not exists posts (
                    post_number integer primary key,
                    text text not null,
                    photo_file_id text
                );
                """
            )
