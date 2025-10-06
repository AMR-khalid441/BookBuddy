# here is the base that all routes begin from 
# the welcome 
from fastapi import FastAPI , APIRouter , Depends
from helpers import Settings , get_settings

base_router= APIRouter(prefix="/api/v1" , tags=["welcome"])

@base_router.get("/")
async def welcome(app_settings:Settings=Depends(get_settings)):
    app_name = app_settings.APP_VERSION
    app_version = app_settings.APP_VERSION
    return {
        "app_name " :app_name,
        "app_version":app_version , 
        "message": "Hello world!"
    }
