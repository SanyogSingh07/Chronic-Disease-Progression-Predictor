from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = Path(r"U.S._Chronic_Disease_Indicators.csv")
MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
