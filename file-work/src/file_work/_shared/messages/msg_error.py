from .msg_base import MsgBase

class MsgError(MsgBase):
    @classmethod
    def file_read(cls, file_path: str, error: str) -> None:
        cls._logger.error(f"Read failed '{file_path}': {error}")

    @classmethod
    def file_write(cls, file_path: str, error: str) -> None:
        cls._logger.error(f"Write failed '{file_path}': {error}")

    @classmethod
    def invalid_extension(cls, extension: str, valid_extensions: list[str]) -> None:
        cls._logger.error(
            f"Invalid extension '{extension}', allowed: {', '.join(valid_extensions)}"
        )

    @classmethod
    def file_not_found(cls, file_path: str) -> None:
        cls._logger.error(f"File not found: '{file_path}'")

    @classmethod
    def file_exists(cls, file_path: str) -> None:
        cls._logger.error(f"File already exists: '{file_path}'")
