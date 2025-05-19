import logging
import logging.config
import json
from pathlib import Path
from typing import Optional, Dict, Any
from colorama import init
from .._internal.color_formatter import ColorFormatter

init(autoreset=True)


class LogManager:
    def __init__(self, config_path: str = "config/logging_config.json"):
        self._config_path = config_path
        self._logger = logging.getLogger("LogManager")

    def setup_logging(self, default_level: int = logging.INFO) -> bool:
        try:
            config_file = Path(self._config_path)
            if not config_file.exists():
                raise FileNotFoundError(f"Logging config file not found at: {self._config_path}")

            with config_file.open('r', encoding='utf-8') as f:
                config = json.load(f)

            has_file_handler = any(
                handler.get("class", "").endswith("FileHandler")
                for handler in config.get("handlers", {}).values()
            )

            if has_file_handler:
                log_dir = Path("logs")
                log_dir.mkdir(exist_ok=True)

            logging.config.dictConfig(config)

            for logger_name in config.get("loggers", {}):
                logger = logging.getLogger(logger_name)
                for handler in logger.handlers:
                    if isinstance(handler, logging.StreamHandler):
                        handler.setFormatter(
                            ColorFormatter(config["formatters"]["default"]["format"])
                        )

            return True
        except json.JSONDecodeError:
            self._logger.error(f"Invalid JSON format in logging config file: {self._config_path}")
        except FileNotFoundError as e:
            self._logger.error(str(e))
        except Exception as e:
            self._logger.error(f"Failed to setup logging: {str(e)}", exc_info=True)
            logging.basicConfig(level=default_level)

        return False