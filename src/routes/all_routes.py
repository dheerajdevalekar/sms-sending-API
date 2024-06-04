from fastapi import APIRouter
from src.routes.send_sms import router as send_sms

router = APIRouter()

router.include_router(send_sms)
