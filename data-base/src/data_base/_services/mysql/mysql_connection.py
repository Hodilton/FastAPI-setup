import mysql.connector
from ..._shared.messages.msg_debug import ConnectionDebug as Debug
from ..._shared.messages.msg_info import ConnectionsInfo as Info
from ..._shared.messages.msg_error import MsgError, ConnectionsError

class MySQLConnection:
    def __init__(self, config: dict):
        self._config = config
        self._connection = None

    def connect(self) -> bool:
        if self._connection:
            Debug.connection_already_established(self._config.get("name"))
            return True
        try:
            self._connection = mysql.connector.connect(
                host=self._config.get("host"),
                user=self._config.get("user"),
                password=self._config.get("password"),
                database=self._config.get("name")
            )
            Info.connection_established(self._config.get("name"))
            return True
        except mysql.connector.DatabaseError as e:
            MsgError.try_action(f"{str(e.msg)}")
            ConnectionsError.connection_established(self._config.get("name"))
            return False

    def is_connected(self) -> bool:
        if self._connection is None:
            return False
        try:
            self._connection.ping(reconnect=False)
            return True
        except mysql.connector.Error as e:
            MsgError.try_action(str(e))
            return False

    def close(self):
        if self._connection:
            self._connection.close()
            Msg.Complete.close_connection(self._config.get("name"))

    @property
    def raw(self):
        return self._connection
