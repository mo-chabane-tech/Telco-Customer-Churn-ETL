import logging
import sqlite3
import pandas as pd
from src.database import DatabaseManager

logger = logging.getLogger(__name__)

def get_churn_stats(db_manager: DatabaseManager, table_name: str) -> pd.DataFrame:
    query = f"""
    select 
        Contract,
        sum(case when Churn = 'Yes' then 1 else 0 end) as Churned_Count,
        count(*) as Total_Count,
        round(sum(case when Churn = 'Yes' then 1 else 0 end) * 100 / count(*), 2) as Churned_Percentage
    from {table_name}
    group by Contract;
    """

    try:
        df = pd.read_sql_query(query, db_manager.conn)
        logger.info("Churn stastistics retrieved successfully.")
        return df
    
    except sqlite3.Error as e:
        logger.error(f"Query execution failed: {e}")
        raise

def get_monthly_charges_stats(db_manager: DatabaseManager, table_name: str) -> pd.DataFrame:
    query = f"""
    select 
        tenure,
        MonthlyCharges,
        Churn
    from {table_name};
    """

    try:
        df = pd.read_sql_query(query, db_manager.conn)
        logger.info("Monthly charges data retrieved successfully.")
        return df
    
    except sqlite3.Error as e:
        logger.error(f"Query execution failed: {e}")
        raise

def get_senior_churn_rate(db_manager: DatabaseManager, table_name: str) -> pd.DataFrame:
    query = f"""
    select 
        case when SeniorCitizen = 1 then 'Senior' else 'Non-Senior' end as Age_Group,
        count(*) as Total_Customers,
        sum(case when Churn = 'Yes' then 1 else 0 end) as Churned_Count,
        round(sum(case when Churn = 'Yes' then 1 else 0 end) * 100 / count(*), 2) as Churn_Rate
    from {table_name}
    group by SeniorCitizen;
    """
    
    try:
        df = pd.read_sql_query(query, db_manager.conn)
        logger.info("Retrieved senior citizen churn analysis.")
        return df
    
    except sqlite3.Error as e:
        logger.error(f"Error fetching senior churn data: {e}")
        raise