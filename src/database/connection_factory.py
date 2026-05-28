import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager


class SqliteConnectionFactory:
    def __init__(self, database_path: str) -> None:
        self.__database_path = database_path

    def create_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.__database_path)
        connection.row_factory = sqlite3.Row
        return connection

    @contextmanager
    def open_connection(self) -> Iterator[sqlite3.Connection]:
        connection = self.create_connection()
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()
