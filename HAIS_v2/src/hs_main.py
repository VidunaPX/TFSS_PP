#from openai import OpenAI
import os

from hs_runModel import hs_get_ai_response

#initializing
my_bot_name = "your_bot_name"

# Setting OpenAI API Key
my_api_key = "API_KEY"

#Functions
def set_open_api_key():
    try:
        os.environ["OPENAI_API_KEY"] = my_api_key
        print("TEST: OpenAI API Key has been set.")
    except Exception as e:
        print("ERR001: An error occurred while setting up the API. Error:" + e)

#Call Model
def get_myModel(UserInput):
    response = hs_get_ai_response(UserInput, my_bot_name)
    return response

UserInput = input("Enter your message: ")
print(get_myModel(UserInput))

    

