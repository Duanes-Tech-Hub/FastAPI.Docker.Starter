from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from util.config import settings
from routers import author, blog

# ---------------------------------------------------------
# App Initialization
# ---------------------------------------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/api/v1/docs",  # Behind proxy convenience
    openapi_url="/api/v1/openapi.json"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom handler for Pydantic validation errors."""
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation failed",
            "errors": exc.errors()
        }
    )

app.include_router(author.router)
app.include_router(blog.router)

@app.get("/api/v1/welcome")
def base_route():
    return {"message": f"Welcome to the FastAPI application in a docker container, {settings.APP_NAME} v{settings.VERSION}!"}
