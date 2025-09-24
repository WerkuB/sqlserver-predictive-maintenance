# SQL Server Predictive Maintenance

This project collects SQL Server performance metrics, preprocesses them,
and applies anomaly detection using machine learning to flag potential issues.

## Steps
1. Configure `.env` with SQL Server details.
2. Run `python -m src.extract` to collect metrics.
3. Run `python -m src.preprocess` to clean data.
4. Run `python -m src.train_model` to train anomaly detection model.

## Requirements
- Python 3.8+
- pyodbc
- pandas
- scikit-learn
- python-dotenv
