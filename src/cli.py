import typer
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from src.config import MODEL_DIR

from src.data.loader import load_data
from src.data.preprocess import preprocess
from src.data.sequence import create_sequences
from src.models.train import train_models

app = typer.Typer()

def detect_columns(df):
    id_candidates = ["patient_id", "id", "patient", "patientid"]
    time_candidates = ["time", "date", "timestamp", "visit"]
    target_candidates = ["progression", "target", "stage", "outcome"]

    id_col = next((c for c in df.columns if c.lower() in id_candidates), None)
    time_col = next((c for c in df.columns if c.lower() in time_candidates), None)
    target_col = next((c for c in df.columns if c.lower() in target_candidates), None)

    if target_col is None:
        target_col = df.columns[-1]

    return id_col, time_col, target_col

@app.command()
def train():
    df = load_data()
    id_col, time_col, target_col = detect_columns(df)
    df = preprocess(df, id_col, time_col, target_col)
    
    # Direct feature and target split (no sequences)
    X = df.drop(columns=[target_col]).values
    y = df[target_col].values
    
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    best_name, best_score = train_models(
        X_train, X_test, y_train, y_test
    )
    
    # Save the scaler for later inference (used by prediction)
    joblib.dump(scaler, MODEL_DIR / "scaler.pkl")
    
    print(f"\nBest Model: {best_name} | R2: {best_score:.3f}")

@app.command()
def predict_disease(disease: str):
    """
    Predict average progression for a disease by filtering patient rows, applying the same preprocessing
    and scaling as during training, and averaging the model predictions.
    """
    import joblib
    from src.config import MODEL_DIR
    from sklearn.preprocessing import MinMaxScaler
    import pandas as pd

    df = load_data()

    # Detect disease column
    disease_col = None
    for col in df.columns:
        if col.lower() in ["disease", "condition", "illness"]:
            disease_col = col
            break
    if disease_col is None:
        print("[Error] Dataset has no disease column → cannot proceed")
        return

    # Filter rows for the requested disease
    df_filtered = df[df[disease_col].str.lower() == disease.lower()]
    if df_filtered.empty:
        print(f"[Error] No records found for disease: {disease}")
        return
    print(f"[Success] Found {len(df_filtered)} patients with {disease}")

    # Detect columns for preprocessing (id, time, target)
    id_col, time_col, target_col = detect_columns(df_filtered)

    # Remove disease column before preprocessing (it is not a feature for the model)
    df_filtered = df_filtered.drop(columns=[disease_col])

    # Apply the same preprocessing as during training
    df_processed = preprocess(df_filtered, id_col, time_col, target_col)

    # Separate features and target
    X = df_processed.drop(columns=[target_col]).values

    # Load model and scaler
    model_files = list(MODEL_DIR.glob("best_model_*.pkl"))
    if not model_files:
        print("[Error] Train model first")
        return
    model = joblib.load(model_files[0])
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")

    # Scale features using the saved scaler
    X = scaler.transform(X)

    # Predict and aggregate
    preds = model.predict(X)
    avg_progression = preds.mean()

    print("\n[Result] Disease Progression Result")
    print(f"Disease: {disease}")
    print(f"Predicted Progression Rate: {avg_progression:.2f}")

