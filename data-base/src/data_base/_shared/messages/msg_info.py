from .msg_base import MsgBase

class ConnectionsInfo(MsgBase):
    @classmethod
    def connection_established(cls, database_name: str) -> None:
        cls._logger.info(f"Connection to database '{database_name}' was successful")

class RepositoriesInfo(MsgBase):
    @classmethod
    def tables_initialized(cls, table_names: list) -> None:
        cls._logger.info(f"Initialized tables: {', '.join(table_names)}")
