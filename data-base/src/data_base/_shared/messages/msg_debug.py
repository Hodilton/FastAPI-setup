from .msg_base import MsgBase

class ConnectionDebug(MsgBase):
    @classmethod
    def connection_already_established(cls, database_name: str) -> None:
        cls._logger.debug(f"Connection to database '{database_name}' already established")

class RepositoriesDebug(MsgBase):
    @classmethod
    def table_initialized(cls, table_name: str) -> None:
        cls._logger.debug(f"Table '{table_name}' initialized with queries successfully")

    @classmethod
    def tables_initialized(cls) -> None:
        cls._logger.debug(f"Tables initialized with queries successfully.")