# IDS706-week12-mlflow [![CI](https://github.com/nogibjj/IDS706-week12-mlflow/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/IDS706-week12-mlflow/actions/workflows/ci.yml)

## Week 12: Use MLflow to Manage an ML Project
### Requirements
- Create a simple machine-learning model
- Use MLflow to manage the project, including tracking metrics
### Grading Criteria
- Model functionality (20 points)
- MLflow tracking (20 points)
### Deliverables
- MLflow project directory
- Document or video demonstrating tracking with MLflow

## Stock Price Prediction with MLflow Overview

This repository hosts the code for a machine learning project aimed at predicting stock prices. Utilizing MLflow, we efficiently manage our ML project lifecycle, including experiment tracking, model tuning, and metric logging.

## Requirements

- Python 3.8+
- MLflow 1.0+
- Pandas, NumPy, scikit-learn
- Historical stock data

## Setup

To get started with this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/nogibjj/IDS706-week12-mlflow.git
cd IDS706-week12-mlflow
pip install -r requirements.txt
```

## Usage
Run the main script to start the training process and log the experiments with MLflow:  `python main.py`

To view the MLflow UI and the experiments:
`mlflow ui`

## Purpose of Project

### Objective

The primary goal of this project is to develop a machine learning model capable of predicting future stock prices based on historical data. The model aims to identify patterns in stock movements and make informed predictions that could aid in investment decisions.

### Data Format

The dataset used consists of historical stock prices which include features like opening price, closing price, the highest price of the day, the lowest price of the day, and trading volume. Each entry is indexed by date, allowing for time-series analysis.

### Steps

The `main.py` script orchestrates the following process:
1. Data Acquisition: It begins by loading historical stock data from the CSV files located in the `data/` directory.
2. Preprocessing: The script then preprocesses this data to format it suitably for training, such as handling missing values, normalizing, and potentially feature engineering.
3. Model Training: The data is split into training and testing sets, and a machine learning model (like a Random Forest Regressor) is trained on the historical data.
4. MLflow Tracking: Throughout the process, MLflow is used to track the experiment, logging important parameters, metrics, and model artifacts.
5. Prediction and Evaluation: Finally, the model is used to make predictions on the test set, and the performance is evaluated to understand the efficacy of the model.

This automated workflow allows for robust experimentation and easy replication of results, with MLflow managing the lifecycle of machine learning experiments.
