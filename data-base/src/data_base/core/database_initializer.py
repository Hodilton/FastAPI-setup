from .._config.database_config_loader import DataBaseConfigLoader
from .._config.tables_config_loader import TablesConfigLoader
from .._config.queries_config_loader import QueriesConfigLoader
from .database_wrapper import DatabaseWrapper

class DatabaseInitializer:
    @staticmethod
    def initialize(config_folder: str) -> DatabaseWrapper | None:
        database_loader = DataBaseConfigLoader(config_folder)
        if not database_loader.load_config():
            return None

        tables_loader = TablesConfigLoader(config_folder)
        if not tables_loader.load_config():
            return None

        queries_loader = QueriesConfigLoader(config_folder)
        queries_dict = {}

        for table_name in tables_loader.tables_config:
            queries = queries_loader.load_config(table_name)
            if queries:
                queries_dict[table_name] = queries

        return DatabaseWrapper(
            database_config=database_loader.database_config,
            tables_config=tables_loader.tables_config,
            queries_dict=queries_dict
        )
