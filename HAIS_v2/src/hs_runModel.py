from openai import OpenAI

def hs_get_ai_response(UserInput):
    try:
        client = OpenAI(
            api_key="API_KEY"
        )

        completion = client.chat.completions.create(
            model= "gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant for high school students, providing factual and helpful information about academics, mental wellbeing, and life skills.",
                },
                {"role": "user", "content": UserInput},
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        # print("ERR003: An error occurred while calling the model. Error: " + str(e))
        return "HAIS-ERROR:" + str(e)
    
#get_ai_response("What is the name of the first president of the United States?")
