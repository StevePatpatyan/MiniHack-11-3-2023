import os
import openai

#get api key from file
openai.api_key_path = ".env"
openai.api_key = os.getenv("OPENAI_API_KEY")

#set behavior
messages = [
    {"role": "system", "content": "You are a person."},
  ]
while True:
    #user prompt
    msg = input()
    #add to bot to answer/remember previous messages
    messages.append({"role": "user", "content": msg})
    #create model
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    #output response
    response = completion.choices[0].message
    print(response.content)