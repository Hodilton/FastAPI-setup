from .._internal.database_bootstrapper import DatabaseBootstrapper
from .._internal.repository_initializer import RepositoryInitializer

class DatabaseBuilder:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def build(self):
        database_bootstrapper = DatabaseBootstrapper(self.config_path)
        if not database_bootstrapper.bootstrap():
            return None

        initializer = RepositoryInitializer(
            bootstrapper.get_database_config(),
            bootstrapper.get_queries_dict(),
        )

        return True
