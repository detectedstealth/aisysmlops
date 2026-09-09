from pydantic import BaseModel, Field


class RiskPredictionRequest(BaseModel):
    age: int = Field(..., examples=[52])
    gender: str = Field(..., examples=["M", "F"])
    city: str = Field(..., examples=["New York"])
    insurance_provider: str = Field(..., examples=["CareOne"])
    chronic_flag: int = Field(..., examples=[1])
    department: str = Field(..., examples=["Cardiology"])
    visit_type: str = Field(..., examples=["ER"])
    doctor_id: int = Field(..., examples=[101])
    length_of_stay_hours: float = Field(..., examples=[48])
    days_since_registration: int = Field(..., examples=[300])
    visit_frequency: float = Field(..., examples=[36.5])
    avg_los_per_patient: float = Field(..., examples=[3])
    visit_month: int = Field(..., examples=[3])
    visit_dayofweek: int = Field(..., examples=[2])