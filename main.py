from log_manager import LogManager
from data_base import DatabaseWrapper, DatabaseInitializer
from file_work import File

def main():
    log_manager = LogManager("config/logging_config.json")
    log_manager.setup_logging()

    database_wrapper = DatabaseInitializer().initialize("config/database")
    database_wrapper.connect()

if __name__ == "__main__":
    main()
