from .BaseController import Base_Controller
from fastapi import UploadFile , File
from models import ResponseSignal
class Data_Controller(Base_Controller):
    def __init__(self):
        super.__init__()
        self.size_scale = 1048576 # convert MB to bytes

    


    def validate_uploaded_file(self , file:UploadFile=File(...)):

        if file.size >self.app_settings.FILE_MAX_SIZE*self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value
        if file.content_type not in self.app_settings.File_allowed_types:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.vale
        

        return True
        