from database.DBAdapter import DBAdapter


class TaskModel:
    def __init__(self, db: DBAdapter, id: int, content: str, done: bool) -> None:
        self.db = self.db
        self.id = id
        self.content = content
        self.done = done

    def save(self):
        self.db()
