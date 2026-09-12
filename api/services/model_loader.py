import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
MODELS_DIR = BASE_DIR / "models"
RISK_MODEL_PATH = MODELS_DIR / "risk_model_complete_pipeline.joblib"
CLAIM_MODEL_PATH = MODELS_DIR / "claim_model_complete_pipeline.joblib"


def load_risk_model():
    if not RISK_MODEL_PATH.exists():
        raise ValueError("Risk model file does not exist")
    model = joblib.load(RISK_MODEL_PATH)
    model_name = "HealthcareRiskModel"
    version = "local-file"
    return model, model_name, version


def load_claim_model():
    if not CLAIM_MODEL_PATH.exists():
        raise ValueError("Claim model file does not exist")
    model = joblib.load(CLAIM_MODEL_PATH)
    model_name = "HealthcareClaimModel"
    version = "local-file"
    return model, model_name, version