from requests import get
from loguru import logger
from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

sms_url = {1: 'http://173.45.76.227/send.aspx'}

router = APIRouter()


class SMSBasemodel(BaseModel):
    contact_num: str
    message: str


@router.post(path="/send_sms_1", tags=["Send SMS"])
def send_sms(sms_data: SMSBasemodel):
    try:
        url_num = 1
        res = get(
            url=sms_url[url_num],
            params={
                'username': 'cian',
                'pass': 'Cian1235',
                'route': 'trans1',
                'senderid': 'IAMCMS',
                'numbers': sms_data.contact_num,
                'message': sms_data.message
            }
        )
        if res.status_code == 200:
            logger.success(f'Send SMS to {sms_data.contact_num}: {sms_data.message}')
            return res.json()
        else:
            logger.info(f'Unable to send SMS to {sms_data.contact_num}: {sms_data.message}')
            raise HTTPException(status_code=res.status_code, detail=res.json())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
