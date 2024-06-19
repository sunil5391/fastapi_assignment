from fastapi import FastAPI
from utils import setup_logger
# import views
from view import views

app = FastAPI()

logger = setup_logger()

logger.info('App started')

app.include_router(views.router)

@app.get('/')
def home():
    return {'message': 'Api is running.....'}