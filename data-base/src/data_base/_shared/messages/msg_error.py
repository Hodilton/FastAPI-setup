from .msg_base import MsgBase

class MsgError(MsgBase):
    @classmethod
    def try_action(cls, exception: str) -> None:
        cls._logger.error(f"{exception}")

class ConfigLoadError(MsgBase):
    @classmethod
    def database_load_config(cls, error: str) -> None:
        cls._logger.error(f"The Database Config was not uploaded: {error}")

    @classmethod
    def tables_load_config(cls, error: str) -> None:
        cls._logger.error(f"The Tables Config was not uploaded: {error}")

    @classmethod
    def table_load_queries(cls, table_name: str, error: str) -> None:
        cls._logger.error(f"Queries for table '{table_name}' was not uploaded: {error}")

class ConnectionsError(MsgBase):
    @classmethod
    def connection_established(cls, database_name: str) -> None:
        cls._logger.error(f"Connection to database '{database_name}' was not successful")

    @classmethod
    def connection_miss(cls, database_name: str) -> None:
        cls._logger.error(f"No connection to database '{database_name}' exists")

class RepositoriesError(MsgBase):
    @classmethod
    def missing_queries(cls, missing_tables: list) -> None:
        error_msg = (
            f"Missing queries for tables: '{', '.join(missing_tables)}'")
        cls._logger.error(error_msg)

    @classmethod
    def table_initialized(cls, table_name: str, error: str) -> None:
        cls._logger.error(f"Failed to initialize table '{table_name}' : {error}")