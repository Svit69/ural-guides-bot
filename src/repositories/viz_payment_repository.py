from datetime import datetime, timezone

from src.database.connection_factory import SqliteConnectionFactory


class VizPaymentRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def get_payment(self, user_id: int) -> dict[str, object] | None:
        with self.__connections.open_connection() as connection:
            row = connection.execute(
                "select * from viz_payments where user_id = ?", (user_id,)
            ).fetchone()
        return dict(row) if row else None

    def save_payment(self, user_id: int, payment: dict[str, str]) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                """
                insert into viz_payments(user_id, payment_id, status, confirmation_url, updated_at)
                values (?, ?, ?, ?, ?)
                on conflict(user_id) do update set payment_id = excluded.payment_id,
                status = excluded.status, confirmation_url = excluded.confirmation_url,
                updated_at = excluded.updated_at
                """,
                (
                    user_id,
                    payment["payment_id"],
                    payment["status"],
                    payment.get("confirmation_url"),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )

    def update_status(self, user_id: int, status: str) -> None:
        with self.__connections.open_connection() as connection:
            connection.execute(
                "update viz_payments set status = ?, updated_at = ? where user_id = ?",
                (status, datetime.now(timezone.utc).isoformat(), user_id),
            )
