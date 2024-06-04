from uvicorn import run
from loguru import logger
from fastapi import FastAPI
from src.routes.all_routes import router

service_port_num = 18457

app = FastAPI(title="Gateway for Sending SMS")
app.include_router(router)


if __name__ == '__main__':
    logger.info("Starting SMS Sending Service....!!!!!")

    run("main:app", host="0.0.0.0", port=service_port_num, reload=True)
