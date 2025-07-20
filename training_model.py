import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

DATA_PATH = "eeg_dummy_dataset.csv"
MODEL_PATH = "eeg_model.joblib"
ENCODER_PATH = "label_encoder.joblib"
TEST_SET_SIZE = 0.2
RANDOM_STATE = 42

def prepare_data(df):
    if 'intent' not in df.columns:
        raise ValueError("The 'intent' column is missing from the dataset.")
    
    features = df.drop('intent', axis=1)
    numeric_features = features.select_dtypes(include=np.number)

    if numeric_features.shape[1] < features.shape[1]:
        dropped_cols = set(features.columns) - set(numeric_features.columns)
        print(f"[Warning] Non-numeric feature columns were found and ignored: {list(dropped_cols)}")

    X = numeric_features
    y = df["intent"]
    
    return X, y

def run_training_pipeline():
    print(f"Loading data from '{DATA_PATH}'...")
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"[Error] Dataset file not found at '{DATA_PATH}'. Please ensure the file exists.")
        return

    print("Preparing data and encoding labels...")
    X, y = prepare_data(df)
    
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    print(f"Splitting data into training/testing sets ({1-TEST_SET_SIZE:.0%}/{TEST_SET_SIZE:.0%})...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, 
        test_size=TEST_SET_SIZE, 
        random_state=RANDOM_STATE,
        stratify=y_encoded  
    )
    print(f"Training set size: {len(X_train)} samples")
    print(f"Testing set size: {len(X_test)} samples")

    print("\nTraining the RandomForestClassifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1)
    clf.fit(X_train, y_train)
    print("Training complete.")

    print("\n--- Model Evaluation ---")
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy on Test Set: {accuracy:.4f}")

    print("\nClassification Report:")
    report = classification_report(
        y_test, 
        y_pred, 
        target_names=label_encoder.classes_,
        zero_division=0
    )
    print(report)
    print("------------------------")

    print(f"\nSaving model to '{MODEL_PATH}'...")
    joblib.dump(clf, MODEL_PATH)

    print(f"Saving label encoder to '{ENCODER_PATH}'...")
    joblib.dump(label_encoder, ENCODER_PATH)
    
    print("\nModel and label encoder saved successfully!")

if __name__ == '__main__':
    run_training_pipeline()
