import os
import openai
openai.api_key_path = "C:\\Users\\steph\\OneDrive\\Desktop\\Projects\\MiniHack 11-3-2023\\.env"
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)
print(response)

