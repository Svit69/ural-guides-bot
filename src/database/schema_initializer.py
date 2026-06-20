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
                    telegram_id integer primary key, username text,
                    full_name text, registered_at text not null
                );
                create table if not exists posts (
                    post_number integer primary key,
                    text text not null,
                    photo_file_id text
                );
                create table if not exists post_media (
                    post_number integer not null, position integer not null,
                    media_type text not null, file_id text not null,
                    primary key (post_number, position)
                );
                create table if not exists feedback (
                    id integer primary key autoincrement,
                    user_id integer,
                    full_name text,
                    text text,
                    media_type text,
                    file_id text,
                    created_at text not null
                );
                """
            )
            connection.execute(
                """
                insert or ignore into post_media
                select post_number, 0, 'photo', photo_file_id
                from posts
                where photo_file_id is not null
                """
            )
