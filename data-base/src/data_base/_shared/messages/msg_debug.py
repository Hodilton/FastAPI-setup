from .msg_base import MsgBase

class ConnectionDebug(MsgBase):
    @classmethod
    def connection_already_established(cls, database_name: str) -> None:
        cls._logger.debug(f"Connection to database '{database_name}' already established")

class ConfigLoadDebug(MsgBase):
    @classmethod
    def database_load_config(cls) -> None:
        cls._logger.debug(f"Database config loaded successfully")

    @classmethod
    def tables_load_config(cls) -> None:
        cls._logger.debug(f"Tables config loaded successfully")

    @classmethod
    def table_load_queries(cls, table_name: str) -> None:
        cls._logger.debug(f"Queries for table '{table_name}' loaded successfully")

class RepositoriesDebug(MsgBase):
    @classmethod
    def table_initialized(cls, table_name: str) -> None:
        cls._logger.debug(f"Table '{table_name}' initialized with queries successfully")

    @classmethod
    def tables_initialized(cls) -> None:
        cls._logger.debug(f"Tables initialized with queries successfully.")