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
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Contract', y='Churn_Percentage', data=df, palette='viridis')
        
        plt.title('Churn Percentage by Contract Type')
        plt.ylabel('Churn Percentage (%)')
        plt.xlabel('Contract Type')

        save_path = Path(config["paths"]["reports_dir"]) / "churn_by_contract.png"
        plt.savefig(save_path)
        logger.info(f"Saved churn analysis plot at {save_path}")

    except Exception as e:
        logger.error(f"Error generating churn plot: {e}")
        raise

def plot_charges_scatter(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', alpha=0.6)

        plt.xlabel('Tenure (Months)')
        plt.ylabel('Monthly Charges ($)')
        plt.title('Monthly Charges vs Tenure')

        save_path = Path(config["paths"]["reports_dir"]) / "charges_vs_tenure.png"
        plt.savefig(save_path)
        logger.info(f"Saved churn analysis plot at {save_path}")

    except Exception as e:
        logger.error(f"Error generating scatter plot: {e}")
        raise