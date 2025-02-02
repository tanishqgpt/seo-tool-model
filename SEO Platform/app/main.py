from fastapi import FastAPI
from app.routes import generation
from app.config.settings import settings
from app.errors import http_error_handler
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_name)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(HTTPException, http_error_handler)

# Include routes
app.include_router(generation.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}