from log_manager import setup_logging
from data_base import DatabaseService

def main():
    setup_logging()

    db = DatabaseService(config_path="config")
    db.connect()

if __name__ == "__main__":
    main()
