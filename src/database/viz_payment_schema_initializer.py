from src.database.connection_factory import SqliteConnectionFactory


class VizPaymentSchemaInitializer:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def initialize_schema(self) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                """
                create table if not exists viz_payments (
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
                create table if not exists viz_access (
                    user_id integer primary key,
                    payment_id text not null,
                    granted_at text not null
                )
                """
            )
            connection.execute(
                """
                insert or ignore into viz_access(user_id, payment_id, granted_at)
                select user_id, payment_id, updated_at from viz_payments
                where status = 'succeeded'
                """
            )
