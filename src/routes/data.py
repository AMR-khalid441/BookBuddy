# this api to upload data itself ;
from fastapi import FastAPI, Depends, APIRouter, UploadFile, File, status
from fastapi.responses import JSONResponse
from helpers import Settings, get_settings
from controllers import DataController
from controllers import ProjectController
import aiofiles
import os
from models import ResponseSignal
import logging

data_router = APIRouter(prefix="/api/v1", tags=["api_v1", "data"])
logger = logging.getLogger('uvicorn.error')


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str, file: UploadFile = File(...),
    app_settings: Settings = Depends(get_settings)
):
    is_valid, signal = await DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signl": signal
            }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = DataController().generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
            return JSONResponse(
                content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
            })
              
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
