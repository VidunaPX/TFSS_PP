from openai import OpenAI
from hs3_operations import call_openai
import gc

#Garbage Collection Enabled
gc.enable()

#Call the OpenAI
def get_answer(user_input):
    answer = call_openai(user_input)
    return answer

#DEBUG ONLY
#user_input = input("Enter your question: ")
#answer = get_answer(user_input)
#print(answer)