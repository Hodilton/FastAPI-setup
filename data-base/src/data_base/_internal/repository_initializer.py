from .._services.mysql.mysql_connection import MySQLConnection
from .._services.mysql.custom_user_repository import CustomUserRepository
from .._internal.database_wrapper import DatabaseWrapper
from data_base._shared.messages.msg_error import RepositoriesError

class RepositoryInitializer:
    def __init__(self, db_config: dict, queries_dict: dict):
        self.db_config = db_config
        self.queries_dict = queries_dict

    def initialize(self) -> DatabaseWrapper:
        connection = MySQLConnection(self.db_config)
        if not connection.connect():
            return None

        repositories = {}
        for table, queries in self.queries_dict.items():
            try:
                if table == "users":
                    repositories[table] = CustomUserRepository(connection.raw, table, queries)
                RepositoriesDebug.table_initialized(table)
            except Exception as e:
                RepositoriesError.table_initialized(table, str(e))
        RepositoriesInfo.tables_initialized(list(repositories.keys()))
        return DatabaseWrapper(connection, repositories, self.db_config.get("name"))
