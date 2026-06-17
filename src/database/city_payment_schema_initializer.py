from src.database.connection_factory import SqliteConnectionFactory


class CityPaymentSchemaInitializer:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def initialize_schema(self) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                """
                create table if not exists city_payments (
                    user_id integer primary key,
                    payment_id text not null,
                    status text not null,
                    confirmation_url text,
                    updated_at text not null
                )
                """
            )
            connection.execute(
                """
                create table if not exists city_access (
                    user_id integer primary key,
                    payment_id text not null,
                    granted_at text not null
                )
                """
            )
