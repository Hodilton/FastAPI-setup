from .msg_base import MsgBase

class MsgInfo(MsgBase):
    @classmethod
    def file_read(cls, file_path: str) -> None:
        cls._logger.info(f"Read successful: '{file_path}'")

    @classmethod
    def file_write(cls, file_path: str, overwrite: bool = False) -> None:
        mode = " (overwrite)" if overwrite else ""
        cls._logger.info(f"Write successful{mode}: '{file_path}'")
