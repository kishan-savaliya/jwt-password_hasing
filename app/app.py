from fastapi import FastAPI
from app.Routes.blog_routs import app

user = FastAPI()

user.include_router(app)
