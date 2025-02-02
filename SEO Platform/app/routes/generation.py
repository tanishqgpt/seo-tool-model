from fastapi import APIRouter, Depends, HTTPException
from app.models.text_generator import TextGenerator
from app.schemas.requests import GenerationRequest
from app.utils.dependencies import get_generator

router = APIRouter()

@router.post("/generate")
async def generate_text(
    request: GenerationRequest,
    generator: TextGenerator = Depends(get_generator)
):
    try:
        generated_text = generator.generate_text(
            prompt=request.prompt,
            max_new_tokens=request.max_length
        )
        return {"response": generated_text}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Text generation failed: {str(e)}"
        )