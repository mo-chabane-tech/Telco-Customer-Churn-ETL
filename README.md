# Telco-Customer-Churn-ETL 📊
An end-to-end ```Python``` data analysis project investigating customer attrition patterns using the Telco Customer Churn dataset. This project demonstrates a modular, production-ready approach to data analytics, integrating ```sqlite3``` for data warehousing, pandas for transformation, and seaborn for business intelligence reporting.

# Business Intelligence Objectives 🎯 
This analysis pipeline is designed to answer critical business questions regarding customer retention:

1. **Contractual Impact**: Does contract length (Month-to-month vs. One year) significantly affect churn rates?
2. **Demographic Segmentation**: Do senior citizens churn at a different rate than non-seniors?
3. **Service Analysis**: Which internet service types (DSL, Fiber Optic) carry the highest risk of churn?
4. **Operational Friction**: Does the payment method (Electronic check vs. Bank transfer) correlate with customer loss?
5. **Customer Lifecycle**: What is the average tenure of customers who leave vs. those who stay?
6. **Support Efficacy**: Does having a Tech Support add-on reduce the likelihood of churn?

# Technical Features 🛠️
- Modern Python Architecture: Fully modular code structure (src/ package) separating concerns (ETL, Database, Analysis, Plotting).
- Type Hinting: 100% type-annotated functions (typing module) for improved code reliability and IDE support.
- Robust Logging: Context-aware logging configured via yaml and dictConfig, capturing detailed run-time information and errors.
- Data Persistence: Utilizes sqlite3 for local data storage, simulating a Data Warehouse environment.
- Automated Reporting: Generates high-resolution .png visualizations for every key insight.

# Project Structure 📁
```
telco_churn_analysis/
├── config/
│   └── config.yaml               
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv 
├── reports/
│   ├── churn_rate.png           
│   └── monthly_charges.png
├── sql/
│   ├── database.db
├── logs/
│   └── app.log                   
├── src
│   ├── __init__.py
│   ├── database.py               
│   ├── etl.py
│   ├── analysis.py       
│   ├── logger_config.py    
│   ├── plotting.py
│   └── utils.py         
├── main.py                       
├── README.md
├── .gitignore
├── LICENSE
└── requirements.txt
```

# Installation & Setup 🚀

1. Clone the Repository
```bash
git clone "https://github.com/mo-chabane-tech/Telco-Customer-Churn-ETL.git"
cd Telco-Customer-Churn-ETL
```

2. Setup Virtual Environment & Install Dependencies
```bash
# Windows
python3.8 -m venv .venv # or 'python -m venv .venv' if python points to 3.8 or higher
.venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

3. Download the Dataset
- Download the ```WA_Fn-UseC_-Telco-Customer-Churn.csv``` file from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
- Place the file inside the ```data```/ directory.

# Usage 🏃
Run the main pipeline script to process data, perform analysis, and generate reports.
```bash
python main.py
```

**Output**
- A SQLite database (sql/database.db) will be created/updated.
- Six visualizations will be saved to the reports/ folder.
- Detailed logs of the process will be written to logs/app.log.

# Sample Insights Generated 📈
- **Contract Analysis**: Typically reveals Month-to-month contracts have significantly higher churn rates compared to 1-2 year contracts.
- **Service Correlation**: Often highlights that Fiber Optic users, despite higher fees, may have higher churn rates than DSL users (likely due to competitors).
- **Tenure**: Generally shows that newer customers (low tenure) are the most likely to leave, emphasizing the need for robust onboarding.

# Tech Stack
- **Python 3.8+**
- **Pandas**: Data manipulation and analysis.
- **SQLite**: Relational database management and query.
- **Seaborn & Matplotlib**: Statistical data visualization.
- **PyYAML**: Configuration management.
- **Logging**: Standard library logging with dictConfig.