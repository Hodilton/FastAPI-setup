from log_manager import LogManager
from data_base import DatabaseWrapper

def main():
    log_manager = LogManager("config/logging_config.json")
    log_manager.setup_logging()

    db = DatabaseWrapper("config")
    db.connect()

if __name__ == "__main__":
    main()
