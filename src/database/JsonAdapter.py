from io import TextIOWrapper
from database.DBAdapter import DBAdapter
import json


class JsonAdapter(DBAdapter):
    def __init__(self, path: str):
        self.cursor: TextIOWrapper | None = None
        self.path: str = path
        self.temp_data: list = []

    def initialize(self):
        pass

    def connect(self):
        try:
            if self.cursor is not None:
                raise Exception("Database already connected")
            self.cursor = open(self.path, "r+")
            raw_data = self.cursor.read()
            if raw_data == "":
                self.cursor.seek(0)
                self.cursor.write("[]")
            else:
                self.temp_data = json.loads(raw_data)
        except Exception as e:
            print(e)

    def read_record(self, id: int) -> list | dict:
        try:
            if self.cursor is None:
                raise Exception("Database not connected")
            self.cursor.seek(0)
            self.temp_data = json.load(self.cursor)
            return self.temp_data[id] if id != -1 else self.temp_data
        except Exception as e:
            print(e)
            return []

    def create_record(self, data: dict):
        try:
            if self.cursor is None:
                raise Exception("Database not connected")
            self.temp_data.append(data)
            self.cursor.seek(0)
            self.cursor.truncate(0)
            self.cursor.write(json.dumps(self.temp_data))
        except Exception as e:
            print(e)

    def delete_record(self, id: int):
        try:
            if self.cursor is None:
                raise Exception("Database not connected")
            self.temp_data.pop(id)
            self.cursor.seek(0)
            self.cursor.truncate(0)
            self.cursor.write(json.dumps(self.temp_data))
        except Exception as e:
            print(e)

    def close(self):
        try:
            if self.cursor is None:
                raise Exception("Database not connected")
            self.cursor.close()
        except Exception as e:
            print(e)
