# pip install huggingface_hub transformers
from transformers import pipeline

# text generation example
generator = pipeline(
    "text-generation",
    model="meta-llama/Llama-4-Scout-17B-16E-Instruct"
)

result = generator("Hello, explain the solar system", max_new_tokens=50)
print(result[0]['generated_text'])
