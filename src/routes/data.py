# this api to upload data itself ;
from fastapi import FastAPI , Depends , APIRouter , UploadFile ,File, status
from fastapi.responses import JSONResponse
from helpers import Settings , get_settings
from controllers import DataController

data_router = APIRouter(prefix="api/v1/data" ,tags=["api_v1" , "data"])

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id:str , file: UploadFile = File(...)
    ,app_settings:Settings =Depends(get_settings)):

    is_valid , signal=DataController().validate_uploaded_file()
    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
              content={
            "signla" : signal}
            )
    


    
