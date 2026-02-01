import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from pathlib import Path
from typing import Dict, Any

sns.set_theme("poster")
sns.set_style("darkgrid")
logger = logging.getLogger(__name__)

def plot_churn_by_contract(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Contract', y='Churned_Percentage', data=df)
        
        plt.title('Churn Percentage by Contract Type')
        plt.ylabel('Churn Percentage (%)')
        plt.ylim(0, 100)
        plt.xlabel('Contract Type')
        plt.tight_layout()

        save_path = Path(config["paths"]["reports_dir"]) / "churn_by_contract.png"
        plt.savefig(save_path)
        logger.info(f"Saved churn analysis plot to {save_path}")

    except Exception as e:
        logger.error(f"Error generating churn plot: {e}")
        raise

def plot_charges_kde(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 8))
        sns.kdeplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', alpha=0.8)

        plt.xlabel('Tenure (Months)')
        plt.ylabel('Monthly Charges ($)')
        plt.title('Monthly Charges vs Tenure')
        plt.tight_layout()

        save_path = Path(config["paths"]["reports_dir"]) / "charges_vs_tenure.png"
        plt.savefig(save_path)
        logger.info(f"Saved churn analysis plot to {save_path}")

    except Exception as e:
        logger.error(f"Error generating kde plot: {e}")
        raise

def plot_senior_churn(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 8))
        sns.barplot(x="Age_Group", y="Churn_Rate", data=df)

        plt.title('Churn Rate: Senior Citizens vs Non-Seniors')
        plt.ylabel('Churn Rate (%)')
        plt.xlabel('Age Group')
        plt.ylim(0, 100)
        plt.tight_layout()

        save_path = Path(config['paths']['reports_dir']) / "senior_churn_rate.png"
        plt.savefig(save_path)
        logger.info(f"Saved senior citizen plot to {save_path}")

    except Exception as e:
        logger.error(f"Error generating senior churn plot: {e}")
        raise

def plot_internet_service_churn(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 8))
        sns.barplot(x="InternetService", y="Churn_Rate", data=df)

        plt.title('Churn Rate by Internet Service')
        plt.ylabel('Churn Rate (%)')
        plt.xlabel('Internet Service')
        plt.ylim(0, 100)
        plt.tight_layout()

        save_path = Path(config['paths']['reports_dir']) / "internet_service_analysis.png"
        plt.savefig(save_path)
        logger.info(f"Saved internet service plot to {save_path}")

    except Exception as e:
        logger.error(f"Error generating internet service churn plot: {e}")
        raise

def plot_payment_method(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Churn_Percentage', y='PaymentMethod', data=df)

        plt.title('Churn Percentage by Payment Method')
        plt.ylabel('')
        plt.xlabel('Churn Percentage (%)')
        plt.xlim(0, 100)
        plt.tight_layout()
        
        save_path = Path(config['paths']['reports_dir']) / "payment_method_churn.png"
        plt.savefig(save_path)
        logger.info(f"Saved payment method plot to {save_path}")

    except Exception as e:
        logger.error(f"Error generating payment method plot: {e}")
        raise