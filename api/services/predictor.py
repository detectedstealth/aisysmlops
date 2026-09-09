import pandas as pd
from api.services.model_loader import load_risk_model, load_claim_model


def predict_risk_result(data: dict):
    model = load_risk_model()
    # Convert data to DataFrame
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]

    response = {
        "prediction": prediction
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict(df)[0]
        if hasattr(probabilities, "tolist"):
            response["probabilities"] = probabilities.tolist()
        else:
            response["probabilities"] = probabilities
    return response


def predict_claim_result(data: dict):
    model = load_claim_model()
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]

    response = {
        "prediction": prediction
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict(df)[0]
        if hasattr(probabilities, "tolist"):
            response["probabilities"] = probabilities.tolist()
        else:
            response["probabilities"] = probabilities
    return response