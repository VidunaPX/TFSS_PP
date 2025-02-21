import openai
from openai import OpenAI


def get_bot_response(user_input,my_bot_name):
    client = OpenAI(
        api_key="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"
    )

    completion = client.chat.completions.create(
        model=my_bot_name,
        store=True,
        messages=[{"role": "user", "content": user_input}],
    )

    print(completion.choices[0].message)


def test_ai_response(UserInput):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        store=True,
        messages=[
            {"role": "user", "content": UserInput},
    ]
)


    return completion.choices[0].message.content

def test(UserInput):
    return(UserInput + ":Testing the OpenAI API...")


#get_bot_response("What is the name of the first president of the United States?")
