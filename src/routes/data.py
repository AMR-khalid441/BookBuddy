# this api to upload data itself ;
from fastapi import FastAPI , Depends , APIRouter , UploadFile ,File
from helpers import Settings , get_settings

data_router = APIRouter(prefix="api/v1/data" ,tags=["api_v1" , "data"])

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id:str , file: UploadFile = File(...)
    ,app_settings:Settings =Depends(get_settings)):
    pass
    
