from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.routers import api
from src.lib import API_VERSION, PROJECT_NAME

app = FastAPI(title=PROJECT_NAME, openapi_url=f'{API_VERSION}/openapi.json')
app.add_middleware(CORSMiddleware)
app.include_router(api.api_router, prefix=API_VERSION)
