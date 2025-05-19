import mysql.connector
from ..._utils.messages import Messages as Msg

class MySQLConnection:
    def __init__(self, config: dict):
        self._config = config
        self._connection = None

    def connect(self) -> bool:
        if self._connection:
            Msg.Error.connection_already_established(self._config.get("database"))
            return True
        try:
            self._connection = mysql.connector.connect(
                host=self._config.get("host"),
                user=self._config.get("user"),
                password=self._config.get("password"),
                database=self._config.get("name")
            )
            Msg.Complete.connection(self._config.get("name"))
            return True
        except mysql.connector.Error as e:
            Msg.Error.try_action(e)
            return False

    def close(self):
        if self._connection:
            self._connection.close()
            Msg.Complete.close_connection(self._config.get("name"))

    @property
    def raw(self):
        return self._connection
