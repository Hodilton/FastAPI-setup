from typing import Optional
import logging

class Messages:
    _logger = logging.getLogger("File-work")

    class Complete:
        @staticmethod
        def file_read(file_path: str) -> None:
            Messages._logger.info(f"Read successful: {file_path}")

        @staticmethod
        def file_write(file_path: str, overwrite: bool) -> None:
            if overwrite:
                Messages._logger.info(f"File write successful (overwrite mode): {file_path}")
            else:
                Messages._logger.info(f"File write successful: {file_path}")

    class Error:
        @staticmethod
        def file_read(file_path: str, error: str) -> None:
            Messages.logger.error(f"Read failed {file_path}: {error}")

        @staticmethod
        def file_write(file_path: str, error: str) -> None:
            Messages._logger.error(f"Write failed {file_path}: {error}")

        @staticmethod
        def invalid_extension(extension: str, valid_extensions: list) -> None:
            Messages._logger.error(
                f"Invalid extension '{extension}', allowed: {valid_extensions}"
            )

        @staticmethod
        def file_not_found(file_path: str) -> None:
            Messages._logger.error(f"File not found: {file_path}")

        @staticmethod
        def file_exists(file_path: str) -> None:
            Messages._logger.error(f"File already exists: {file_path}")
