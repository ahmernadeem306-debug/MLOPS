import os
import mlflow
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_and_track_model():
    # 1. MLflow Experiment ka naam set karein
    mlflow.set_experiment("Mera_MLOps_Sentiment_Project")
    
    # Dummy data generator (Jaise purelogics bootcamp ya real system mein hota hai)
    X = np.random.rand(100, 10)
    y = np.random.randint(0, 2, 100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # 2. Hyperparameters define karein (Inhe badal kar hum multiple runs check karte hain)
    hyperparams = {
        "C": 0.5,
        "max_iter": 200,
        "solver": "liblinear"
    }
    
    # 3. MLflow Run start karein
    with mlflow.start_run(run_name="Logistic_Regression_Base_Run") as run:
        # Model initialization and training
        model = LogisticRegression(**hyperparams)
        model.fit(X_train, y_train)
        
        # Calculate metric
        accuracy = model.score(X_test, y_test)
        
        # --- MLOps Logging Engine ---
        # Parameters track karein
        mlflow.log_params(hyperparams)
        
        # Metrics track karein
        mlflow.log_metric("accuracy", accuracy)
        
        # Actual Trained Model Weights save (log) karein
        mlflow.log_model(model, artifact_path="sentiment_logistic_model")
        
        print(f"Run Complete! Model logged successfully with Accuracy: {accuracy}")
        return run.info.run_id

if __name__ == "__main__":
    train_and_track_model()
