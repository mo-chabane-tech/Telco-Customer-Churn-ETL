import logging
import sys
from pathlib import Path
from src.utils import get_config, ensure_dir
from src.plotting import plot_charges_kde, plot_churn_by_contract, plot_senior_churn, plot_internet_service_churn
from src.logger_config import setup_logger
from src.etl import extract, tranform, load
from src.database import DatabaseManager
from src.analytics import get_churn_stats, get_monthly_charges_stats, get_senior_churn_rate, get_internet_service_churn

def main():
    db_manager = None

    try:
        config = get_config()

    except Exception as e:
        print(f"Critical: Failed to load config: {e}")
        sys.exit(1)

    table_name = config["tables"]["table_name"]

    try:
        setup_logger(config)
        logger = logging.getLogger(__name__)
        logger.info("="*20)
        logger.info("Starting Telco Churn Analysis Pipeline.")
        logger.info("="*20)

    except Exception as e:
        print(f"Critical: Failed to set up logger: {e}")
        sys.exit(1)

    try:
        db_path = Path(config["paths"]["database"])
        ensure_dir(db_path.parent)
        db_manager = DatabaseManager(db_path)
        db_manager.connect()

    except Exception as e:
        logger.critical(f"Database connection failed: {e}")
        sys.exit(1)

    try:
        df = extract(Path(config["paths"]["data"]))
        df_cleaned = tranform(df)
        load(table_name, df_cleaned, db_manager)
        
    except Exception as e:
        logger.critical(f"ETL failed: {e}")
        sys.exit(1)

    try:
        logger.info("Beginning analysis pipeline.")

        df_churn = get_churn_stats(db_manager, table_name)
        plot_churn_by_contract(df_churn, config)

        df_charges = get_monthly_charges_stats(db_manager, table_name)
        plot_charges_kde(df_charges, config)

        df_senior_churn = get_senior_churn_rate(db_manager, table_name)
        plot_senior_churn(df_senior_churn, config)   

        df_internet_service_churn = get_internet_service_churn(db_manager, table_name)
        plot_internet_service_churn(df_internet_service_churn, config) 

    except Exception as e:
        logger.critical(f"Failed analysis phase: {e}")
        sys.exit(1)

    finally:
        db_manager.close()
        logger.info("Pipeline over.")

if __name__ == "__main__":
    main()