from ..._utils.messages import Messages

class MySQLTableRepository:
    def __init__(self, connection, table_name: str, queries: dict):
        self.connection = connection
        self.table_name = table_name
        self.queries = queries

    def execute(self, query: str, params: tuple = ()) -> int:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount

    def fetch(self, query: str, params: tuple = (), fetch_mode="one"):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone() if fetch_mode == "one" else cursor.fetchall()

    def create(self):
        return self.execute(self.queries["create"])

    def drop(self):
        return self.execute(self.queries["drop"])

    def insert(self, data: tuple):
        return self.execute(self.queries["insert"], data)

    def update(self, data: tuple, condition: tuple):
        return self.execute(self.queries["update"], (*data, *condition))

    def delete(self, name: str, condition: tuple):
        return self.execute(self.queries["delete"][name], condition)
