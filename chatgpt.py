#! /usr/bin/env python3

import openai

def query_chatgpt(openai_api_key, prompt):
    openai.api_key = openai_api_key
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or another model you wish to use
            prompt=prompt,
            max_tokens=2500
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"
