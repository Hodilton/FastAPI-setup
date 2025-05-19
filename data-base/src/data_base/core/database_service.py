from .._config.config_loader import JSONConfigLoader
from .._services.mysql.mysql_connection import MySQLConnection as Connection
from .._services.mysql.mysql_table_repository import MySQLTableRepository
from .._utils.messages import Messages as Msg

class DatabaseService:
    def __init__(self, config_path: str):
        self._config_loader = JSONConfigLoader(config_path)
        self._connection = None
        self._tables_config = None
        self._repositories = {}

    def connect(self):
        db_config = self._config_loader.load("database_config").get("database", {})
        self._connection = Connection(db_config)
        if not self._connection.connect():
            return False

        self._tables_config = self._config_loader.load("tables_config").get("tables", {})
        for table_name in self._tables_config:
            queries = self._config_loader.load(f"queries/{table_name}")
            self._repositories[table_name] = MySQLTableRepository(
                self._connection.raw, table_name, queries
            )
            Msg.Complete.table_initialized(table_name)
        return True

    def reset(self):
        for repo in reversed(self._repositories.values()):
            repo.drop()
        for repo in self._repositories.values():
            repo.create()

    def close(self):
        if self._connection:
            self._connection.close()

    def table(self, name: str):
        return self._repositories.get(name)
