from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.config.settings import settings

class TextGenerator:
    def __init__(self):
        self.device = torch.device(settings.device)
        self.tokenizer = None
        self.model = None
        self.initialize_model()

    def initialize_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(settings.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                settings.model_name,
                torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
                attn_implementation="flash_attention_2"  # Enable Flash Attention
            )
            
            if not self.tokenizer.pad_token:
                self.tokenizer.pad_token = self.tokenizer.eos_token
                
            self.model.to(self.device)
            self.model.eval()
        except Exception as e:
            raise RuntimeError(f"Model initialization failed: {str(e)}")

    def generate_text(self, prompt: str, max_new_tokens: int = None) -> str:
        try:
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                truncation=True,
                max_length=4096
            ).to(self.device)

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens or settings.max_new_tokens,
                temperature=settings.temperature,
                top_p=settings.top_p,
                pad_token_id=self.tokenizer.eos_token_id
            )

            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            raise RuntimeError(f"Generation failed: {str(e)}")