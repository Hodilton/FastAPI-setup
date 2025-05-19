import logging

class Messages:
    class Complete:


        @staticmethod
        def close_connection(db_path):
            Messages._logger.info(f"✅ Connection to database '{db_path}' was successful close.")

        @staticmethod
        def create_db(db_path):
            Messages._logger.info(f"✅ Database {db_path} has been created.")

        @staticmethod
        def delete_db(db_path):
            Messages._logger.info(f"✅ Database {db_path} has been deleted.")

        @staticmethod
        def table_creating(table_name):
            Messages._logger.info(f"✅ Table '{table_name}' created successfully.")

        @staticmethod
        def table_droping(table_name):
            Messages._logger.info(f"✅ Table '{table_name}' dropped successfully.")

    class Error:
        @staticmethod
        def db_path():
            Messages._logger.error("❌ Invalid database path configuration.")

        @staticmethod
        def create_db(db_path):
            Messages._logger.error(f"❌ Failed to create database '{db_path}'.")

        @staticmethod
        def delete_db(db_path):
            Messages._logger.error(f"❌ Failed to delete database '{db_path}'.")

        @staticmethod
        def db_already_exist(db_path):
            Messages._logger.error(f"❌ Database '{db_path}' already exists.")

        @staticmethod
        def db_file_found(db_path):
            Messages._logger.error(f"❌ Database file '{db_path}' not found.")



        @staticmethod
        def table_found(table_name):
            Messages._logger.error(f"❌ Table '{table_name}' not found in configuration.")

        @staticmethod
        def table_already_exist(table_name):
            Messages._logger.error(f"❌ Table '{table_name}' already exists.")

        @staticmethod
        def table_creating(table_name):
            Messages._logger.error(f"❌ Failed to create table '{table_name}'.")

        @staticmethod
        def table_droping(table_name):
            Messages._logger.error(f"❌ Failed to drop table '{table_name}'.")

        @staticmethod
        def data_inserting(table_name):
            Messages._logger.error(f"❌ Failed to insert data into table '{table_name}'.")

        @staticmethod
        def data_updating(table_name):
            Messages._logger.error(f"❌ Failed to update data in table '{table_name}'.")

        @staticmethod
        def data_deleting(table_name):
            Messages._logger.error(f"❌ Failed to delete data from table '{table_name}'.")

        @staticmethod
        def data_fetching(table_name):
            Messages._logger.error(f"❌ Failed to fetch data from table '{table_name}'.")
