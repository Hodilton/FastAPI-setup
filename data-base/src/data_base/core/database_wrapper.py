from .._services.mysql.mysql_connection import MySQLConnection
from .._services.mysql.mysql_table_repository import MySQLTableRepository
from .._shared.messages.msg_error import ConnectionsError, RepositoriesError
from .._shared.messages.msg_debug import RepositoriesDebug
from .._shared.messages.msg_info import RepositoriesInfo

class DatabaseWrapper:
    def __init__(self, database_config: dict, tables_config: dict, queries_dict: dict):
        self._database_config = database_config
        self._tables_config = tables_config
        self._queries_dict = queries_dict

        self._repositories = {}
        self._connection = None

    def connect(self) -> None:
        self._connection = MySQLConnection(self._database_config)
        if self._connection.connect():
            self._initialize_repositories()

    def _initialize_repositories(self) -> None:
        if not self._connection or not self._connection.is_connected():
            ConnectionsError.connection_miss(self._database_config.get("name"))
            return

        missing_queries = [table for table in self._tables_config if table not in self._queries_dict]
        if missing_queries: RepositoriesError.missing_queries(missing_queries)

        initialized_tables = []
        for table_name, queries in self._queries_dict.items():
            try:
                self._repositories[table_name] = MySQLTableRepository(
                    self._connection.raw, table_name, queries
                )
                initialized_tables.append(table_name)
                RepositoriesDebug.table_initialized(table_name)
            except Exception as e:
                RepositoriesError.table_initialized(table_name, str(e))
        RepositoriesInfo.tables_initialized(initialized_tables)

    def table(self, name: str):
        if not self._connection or not self._connection.is_connected():
            ConnectionsError.connection_miss(self._database_config.get("name"))
            return

        return self._repositories.get(name)

    def reset(self):
        if not self._connection or not self._connection.is_connected():
            ConnectionsError.connection_miss(self._database_config.get("name"))
            return

        for repo in reversed(self._repositories.values()):
            repo.drop()
        for repo in self._repositories.values():
            repo.create()

    def close(self):
        if not self._connection or not self._connection.is_connected():
            ConnectionsError.connection_miss(self._database_config.get("name"))
            return

        if self._connection:
            self._connection.close()
