# from time import sleep
from requests import get
from loguru import logger
# from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

sms_url = {1: 'http://173.45.76.227/send.aspx'}

router = APIRouter()


class SMSBasemodel(BaseModel):
    contact_num: list
    message: str


@router.post(path="/send_sms_1", tags=["Send SMS"])
def send_sms(sms_data: SMSBasemodel):
    url_num = 1
    try:
        return_data = {}
        m = sms_data.message
        for each_num in sms_data.contact_num:
            res = get(
                url=sms_url[url_num],
                params={
                    'username': 'cian',
                    'pass': 'Cian1235',
                    'route': 'trans1',
                    'senderid': 'IAMCMS',
                    'numbers': each_num,
                    'message': sms_data.message
                },
                timeout=3
            )
            if res.status_code == 200:
                logger.success(f'Send SMS to {each_num}: {sms_data.message}')
                return_data.update({each_num: {'status_code': res.status_code, 'json_data': res.json()}})
            else:
                logger.info(f'Unable to send SMS to {each_num}: {sms_data.message}')
                return_data.update({each_num: {'status_code': res.status_code, 'json_data': res.json()}})
            # sleep(1)
        return return_data
    except Exception as e:
        logger.error(f'Error to send SMS to {sms_data.contact_num}-{sms_data.message}: {e}')
        raise HTTPException(status_code=500, detail=f'{e}')
