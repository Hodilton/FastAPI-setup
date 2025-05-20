from .mysql.mysql_table_repository import MySQLTableRepository

class Repository(MySQLTableRepository):
    def fetch_one(self, query_name: str, params: tuple):
        query = self.queries.get("fetch", {}).get(query_name)
        if query:
            return self.fetch(query, params, fetch_mode="one")
        return None

    def fetch_all(self, query_name: str, params: tuple = ()):  # по умолчанию пустой кортеж
        query = self.queries.get("fetch", {}).get(query_name)
        if query:
            return self.fetch(query, params, fetch_mode="all")
        return []
