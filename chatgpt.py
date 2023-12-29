#! /usr/bin/env python3

import openai

def query_chatgpt(openai_api_key, prompt, max_tokens=3000):
    openai.api_key = openai_api_key
    
    while True:
        try:
            # Ensure the prompt length doesn't exceed the max_tokens limit
            if len(prompt) > max_tokens:
                prompt = prompt[-max_tokens:]
            
            response = openai.Completion.create(
                engine="text-davinci-003",  # "gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
            # return response.choices[0].message['content'].strip()
        except openai.error.OpenAIError as e:
            error_message = str(e)
            if "Too many tokens" in error_message:
                # Truncate the beginning of the prompt and retry
                prompt = prompt[-(max_tokens // 2):]
            else:
                return f"An error occurred: {error_message}"
