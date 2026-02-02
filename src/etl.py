import pandas as pd
import logging
from src.utils import ensure_dir, sqlite3_dtype_map
from src.database import DatabaseManager
from pathlib import Path

logger = logging.getLogger(__name__)

def extract(data_path: Path) -> pd.DataFrame:
    ensure_dir(data_path.parent)

    try:
        df = pd.read_csv(data_path)
        logger.info(f"Data from {data_path} has been extracted successfully.")
        return df
    
    except FileNotFoundError:
        logger.error(f"File not found {data_path}")
        raise

    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        raise

def transform(df: pd.DataFrame) -> pd.DataFrame: 
    try:
        df["TotalCharges"] = df["TotalCharges"].fillna(0)
        logger.info("Data Transformed successfully.")
        return df
    
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise

def load(table_name: str, df: pd.DataFrame, db_manager: DatabaseManager) -> None:
    try:
        sql_cols = [(col, sqlite3_dtype_map(str(dtype))) for col, dtype in df.dtypes.items()]
        db_manager.create_table(table_name, sql_cols)
        db_manager.insert_data(df, table_name)
        logger.info("Data has been loaded to the database successfully.")

    except Exception as e:
        logger.error(f"Error loading data to database: {e}")
        raise