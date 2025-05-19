from .msg_base import MsgBase

class MsgDebug(MsgBase):
    @classmethod
    def file_read(cls, file_path: str) -> None:
        cls._logger.debug(f"Read successful file './{file_path}'")

    @classmethod
    def file_write(cls, file_path: str, overwrite: bool = False) -> None:
        if overwrite:
            cls._logger.debug(f"Write successful file './{file_path}'")
        else:
            cls._logger.debug(f"Write successful with mode [overwrite] file './{file_path}'")
