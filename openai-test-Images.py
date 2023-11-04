import os
import openai
openai.api_key_path = "C:\\Users\\steph\\OneDrive\\Desktop\\Projects\\MiniHack 11-3-2023\\.env"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
print(response)