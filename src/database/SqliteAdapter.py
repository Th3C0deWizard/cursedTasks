from DBAdapter import DBAdapter
import sqlite3


class SqliteAdapter(DBAdapter):
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.cursor: sqlite3.Cursor | None = None
        self.connection: sqlite3.Connection | None = None

    def connect(self) -> None:
        try:
            if self.connection is not None:
                raise sqlite3.Error("Already connected")
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)

    def close(self) -> None:
        try:
            if self.connection is None:
                raise sqlite3.Error("No connection to close")
            self.connection.close()
        except sqlite3.Error as e:
            print(e)

    def create_record(self, data: dict) -> None:
        try:
            if self.cursor is None or self.connection is None:
                raise sqlite3.Error("No cursor to execute")
            self.cursor.execute(
                "INSERT INTO tasks () VALUES (?, ?, ?, ?)",
                (data["name"], data["surname"], data["phone_number"], data["email"]),
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
