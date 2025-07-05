from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
from core.mcp import MCPMessage

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # ✅ no access needed

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

def generate_response(mcp_msg):
    context_chunks = mcp_msg.payload["top_chunks"]
    user_query = mcp_msg.payload["query"]

    prompt = "\n".join(context_chunks) + f"\n\nUser Question: {user_query}\nAnswer:"

    outputs = generator(
    prompt,
    max_new_tokens=512,
    temperature=0.7,
    do_sample=True,  # ✅ explicitly enable sampling
    top_k=50,
    top_p=0.95
    )
    answer = outputs[0]['generated_text'].split("Answer:")[-1].strip()

    return {
        "answer": answer,
        "sources": context_chunks
    }
