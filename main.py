from log_manager import LogManager
from data_base import DatabaseBuilder
from file_work import File

def main():
    log_manager = LogManager("config/logging_config.json")
    log_manager.setup_logging()

    db = DatabaseBuilder("config/database").build()
    
    # if db and db.is_connected:
    #     user_repo = db.table("users")
    #     user = user_repo.fetch_one("by_id", (1,))
    #     all_users = user_repo.fetch_all("all")

if __name__ == "__main__":
    main()
