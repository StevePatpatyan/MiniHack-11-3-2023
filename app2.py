import os
import openai
import speech_recognition as sr


# get api key from file
openai.api_key_path = ".env"
openai.api_key = os.getenv("OPENAI_API_KEY")

# initialize speech recognizer
recognizer = sr.Recognizer()
# set behavior
messages = [
    {"role": "system", "content": "You are a person."},
]
while True:
    # speech rec code courtesy of geeksforgeeks
    # use the microphone as source for input.
    with sr.Microphone() as source:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        print("Speak :)")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)

        # listens for the user's input
        audio = recognizer.listen(source)

        # Using google to recognize audio
        text = recognizer.recognize_google(audio)
    # add to bot to answer/remember previous messages
    messages.append({"role": "user", "content": text})
    # create model
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    # output response
    response = completion.choices[0].message
    print(response.content)
