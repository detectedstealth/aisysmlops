import pandas as pd
from api.services.model_loader import load_risk_model, load_claim_model
from monitoring.logger import log_prediction


def predict_risk_result(data: dict):
    model, model_name, model_version = load_risk_model()
    # Convert data to DataFrame
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]
    prediction_str = str(prediction)

    response = {
        "prediction": prediction_str
    }

    # Logging
    log_prediction(
        model_name=model_name,
        model_version=model_version,
        input_data=data,
        prediction=prediction_str
    )


    if hasattr(model, "predict_proba"):
        probabilities = model.predict(df)[0]
        if hasattr(probabilities, "tolist"):
            response["probabilities"] = probabilities.tolist()
        else:
            response["probabilities"] = probabilities
    return response


def predict_claim_result(data: dict):
    model, model_name, model_version = load_claim_model()
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]
    prediction_str = str(prediction)

    response = {
        "prediction": prediction_str
    }

    log_prediction(
        model_name=model_name,
        model_version=model_version,
        input_data=data,
        prediction=prediction_str
    )

    if hasattr(model, "predict_proba"):
        probabilities = model.predict(df)[0]
        if hasattr(probabilities, "tolist"):
            response["probabilities"] = probabilities.tolist()
        else:
            response["probabilities"] = probabilities
    return response