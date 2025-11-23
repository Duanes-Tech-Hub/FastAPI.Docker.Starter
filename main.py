from fastapi import FastAPI, Request

from util.config import settings
from model.schemas import UserInput, APIResponse


# ---------------------------------------------------------
# App Initialization
# ---------------------------------------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/api/docs",  # Behind proxy convenience
    openapi_url="/api/openapi.json"
)

@app.get("/api/welcome")
def base_route():
    return {"message": f"Welcome to the FastAPI application in a docker container, {settings.APP_NAME} v{settings.VERSION}!"}
