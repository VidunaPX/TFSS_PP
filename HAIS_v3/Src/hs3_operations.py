from openai import OpenAI

#Call the OpenAI
def call_openai(user_input):
    client = OpenAI(
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:personalproject:tfss-ib-pp-hais:AiUdxRjH",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return completion.choices[0].message.content

#user_input = input("Enter your question: ")
#answer = call_openai(user_input)
#print(answer)