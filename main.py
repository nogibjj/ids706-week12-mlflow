import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def execute_stock_prediction_experiment():
    """Execute a stock prediction experiment, log with mlflow."""
    # Load the dataset
    stock_data = pd.read_csv("data/stock_data.csv")

    # Define features and target
    stock_data['Previous_Close'] = stock_data['Close'].shift(1)
    stock_data = stock_data.dropna()
    features = stock_data[['Previous_Close']]
    target = stock_data['Close']

    # Split the dataset
    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.25, random_state=0
    )

    # Initialize the model
    stock_model = RandomForestRegressor(n_estimators=10, random_state=0)

    # Fit the model
    stock_model.fit(features_train, target_train)

    # Predict and evaluate
    target_predicted = stock_model.predict(features_test)
    error = mean_squared_error(target_test, target_predicted)

    # MLflow tracking
    with mlflow.start_run():
        mlflow.log_param("model_type", "RandomForestRegressor")
        mlflow.log_param("dataset_path", "data/stock_data.csv")
        mlflow.log_metric("mean_squared_error", error)
        mlflow.sklearn.log_model(stock_model, "model")

# Run the experiment
if __name__ == "__main__":
    execute_stock_prediction_experiment()
