from fastapi import FastAPI
from routes.user import user

app = FastAPI()                 #Create object of fast api

app.include_router(user)

 