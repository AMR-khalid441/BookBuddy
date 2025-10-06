from fastapi import FastAPI
from routes import base_router , data_router
# i developed this app using MVC Design pattern
app = FastAPI()
app.include_router(base_router)
app.include_router(data_router)