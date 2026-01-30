import sqlite3
import logging
import pandas as pd
from pathlib import Path
from src.utils import ensure_dir
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)

class DatabaseManager():
    def __init__(self, path: Path) -> None:
        self.path = path
        self.conn = Optional[sqlite3.Connection]

    def connect(self):
        try:
            ensure_dir(self.path.parent)
            self.conn = sqlite3.connect(self.path)
            logger.info(f"Connected to the database at {self.path}")

        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            raise

    def close(self) -> None:
        if(self.conn):
            self.conn.close()
            logger.info("Database connection closed.")

    def check_connection(self):
        if(not self.conn):
            logger.error("No database connection.")
            raise

    def create_table(self, table_name: str, columns: List[Tuple[str, str]]) -> None:
        self.check_connection()

        cols_def = ", ".join([f"{col} {dtype}" for col, dtype in columns])
        table_deletion_query = f"drop table if exists {table_name};"
        table_creation_query = f"create table {table_name}({cols_def});"

        try:
            cursor = self.conn.cursor()
            cursor.execute(table_deletion_query)
            cursor.execute(table_creation_query)
            self.conn.commit()
            logger.info(f"Table {table_name} has been created successfully.")

        except sqlite3.Error as e:
            logger.error(f"Error creating table {table_name}: {e}")
            raise

    def insert_data(self, df: pd.DataFrame, table_name: str) -> None:
        self.check_connection()

        try:
            df.to_sql(table_name, self.conn, if_exists="append", index=False)
            self.conn.commit()
            logger.info(f"{len(df)} rows have been inserted into {table_name}")

        except sqlite3.Error as e:
            logger.error(f"Error inserting data to database: {e}")
            raise