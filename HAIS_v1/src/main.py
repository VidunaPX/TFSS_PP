#from openai import OpenAI
import os
from run_model import get_ai_response

#initializing
my_bot_name = "YOUR_BOT_NAME"

# Setting OpenAI API Key
my_api_key = "YOUR_API_KEY"

#Functions
def set_open_api_key():
    try:
        os.environ["OPENAI_API_KEY"] = my_api_key
        print("OpenAI API Key has been set.")
    except Exception as e:
        print("ERR001: An error occurred while setting up the API. Error:" + e)

#Call Model
def get_myModel(UserInput):
    response = get_ai_response(UserInput, my_bot_name)
    return response
    

