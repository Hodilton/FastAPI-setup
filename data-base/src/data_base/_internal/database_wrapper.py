from data_base._shared.messages.msg_error import ConnectionsError

class DatabaseWrapper:
    def __init__(self, connection, repositories: dict, db_name: str):
        self._connection = connection
        self._repositories = repositories
        self._db_name = db_name

    def connect(self):
        if not self._connection.is_connected():
            self._connection.connect()

    def table(self, name: str):
        if not self._connection.is_connected():
            ConnectionsError.connection_miss(name)
            return None
        return self._repositories.get(name)

    def reset(self):
        if not self._connection.is_connected():
            ConnectionsError.connection_miss("reset")
            return
        for repo in reversed(self._repositories.values()):
            repo.drop()
        for repo in self._repositories.values():
            repo.create()

    def close(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()

    @property
    def is_connected(self):
        return self._connection.is_connected()

    @property
    def database_name(self):
        return self._db_name
