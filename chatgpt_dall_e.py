#! /usr/bin/env python3

from my_secrets import openai_key
import openai
from chatgpt import query_chatgpt 
import requests
from PIL import Image
import random
import re

openai.api_key = openai_key

def generate_character_image(
    description="He's the king from Lord of the Rings", 
    character_race="Human", 
    character_class="Ranger", 
    character_name="Aragorn II Elessar", 
    background_name=None,
    character_gender='Male',
    character_age=35,
    background_features=None,
    background_equipment=None,
    image_style='photo-realistic', 
    image_size='1024x1024',
    dall_e_model='dall_e_2',
    number_of_images=1,
    ):
    chatgpt_dall_e_prompt_raw = f"""
Optimize the following query so that it will create a well constructed query to create a DALL-E image - just provide me the new prompt and include as much details form what I originally provided:
'''
Create a {image_style} style collage of a dnd 5e character, specifically for a {character_gender}, {character_age} year old, {character_race} {character_class}. 
Their background is: {background_name}
Their features are: {background_features}
Their equipment includes: {background_equipment}
Here is more descriptive traits: {description} 
'''
"""
    # input(chatgpt_dall_e_prompt_raw)
    chatgpt_dall_e_prompt = query_chatgpt(openai_key, chatgpt_dall_e_prompt_raw)
    chatgpt_dall_e_prompt += f" Emphasize the image on the race [{character_race}] and class [{character_class}] of the character. The image should be a collage with three distinct sections: the character's face at an angle, a full head-to-toe view of the character from the front, and a full head-to-toe view from the rear. These views are intended to showcase the character's clothing and gear in detail."
    # input(chatgpt_dall_e_prompt)
    chatgpt_dall_e_prompt = chatgpt_dall_e_prompt.strip()
    chatgpt_dall_e_prompt =  re.sub(r'[ ]+', ' ', chatgpt_dall_e_prompt)

    
    response = openai.Image.create(
    model=dall_e_model,
    prompt=chatgpt_dall_e_prompt,
    n=number_of_images,
    size=image_size
    )

    image_url = response['data'][0]['url']

    filename = f"./characters/{character_race} {character_class} ({character_name}).png"

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

        # image = Image.open(f"./characters/{character_name}.png")
        # image.show()

    else:
        print(f"Failed to retrieve content from {image_url}")


