from fastapi import UploadFile
from helpers.config import Settings, get_settings
from models import ResponseSignal
from .BaseController import BaseController


class DataController(BaseController):
    def __init__(self):
        self.size_scale = 1048576  # 1 MB in bytes
        super().__init__()


    async def validate_uploaded_file(self, file: UploadFile):
        # ✅ Check file size
        
        if self.app_settings.FILE_MAX_SIZE > self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        # ✅ Check file type (optional example)
        
        if file.content_type not in get_settings().FILE_ALLOWED_TYPES :
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        return True ,ResponseSignal.FILE_UPLOAD_SUCCESS.value
