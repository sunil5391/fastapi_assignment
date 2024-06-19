from fastapi import FastAPI
from utils import setup_custom_logger
# import views
from view import views

app = FastAPI()

logger = setup_custom_logger()

logger.info('App started')

app.include_router(views.router)

@app.get('/')
def home():
    logger.info('Api is up and running!!!')
    return {'message': 'Api is up and running!!!'}