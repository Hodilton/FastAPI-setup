from .config_loader_base import ConfigLoaderBase
from .._shared.messages.msg_debug import ConfigLoadDebug as Debug
from .._shared.messages.msg_error import ConfigLoadError as Error
from file_work import File

class TablesConfigLoader(ConfigLoaderBase):
    def __init__(self, config_folder: str):
        super().__init__(config_folder)
        self.tables_config = None

    def load_config(self) -> bool:
        config_path = f"{self.config_folder}/tables_config.json"
        try:
            config = File.read(file_path=config_path)
            self.tables_config = config.get('tables', {})
            Debug.tables_load_config()
            return True
        except Exception as e:
            Error.tables_load_config(str(e))
            return False
