from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def http_error_handler(_, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

class GenerationError(Exception):
    """Base exception for generation errors"""