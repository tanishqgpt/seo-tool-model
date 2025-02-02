from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Deepseek API"
    model_name: str = "deepseek-ai/deepseek-coder-1.3b-instruct"
    max_new_tokens: int = 100
    temperature: float = 0.7
    top_p: float = 0.9
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    
    class Config:
        env_file = ".env"

settings = Settings()