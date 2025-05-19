from .config_loader_base import ConfigLoaderBase
from .._shared.messages.msg_debug import ConfigLoadDebug as Debug
from .._shared.messages.msg_error import ConfigLoadError as Error
from file_work import File

class QueriesConfigLoader(ConfigLoaderBase):
    def __init__(self, config_folder: str):
        super().__init__(config_folder)

    def load_config(self, table_name):
        config_path = f"{self.config_folder}/queries/{table_name}.json"
        try:
            config = File.read(file_path=config_path)
            table_config = config.get('queries', {})
            Debug.table_load_queries(table_name)
            return table_config
        except Exception as e:
            Error.table_load_queries(table_name, str(e))
            return None
