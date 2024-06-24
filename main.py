from fastapi import FastAPI
from helper_functions import setup_logger
from view import views

app = FastAPI()

logger = setup_logger()

logger.info('App started')

app.include_router(views.router)

@app.get('/')
def home():
    return {'message': 'Api is executing.....'}
