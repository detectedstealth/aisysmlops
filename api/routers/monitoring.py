from fastapi import APIRouter
from monitoring.drift_monitor import run_psi_monitor

router = APIRouter()

@router.get("/psi")
async def get_psi():
    return run_psi_monitor()