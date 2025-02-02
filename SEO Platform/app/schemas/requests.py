from pydantic import BaseModel, Field

class GenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)
    max_length: int = Field(100, ge=1, le=1000)