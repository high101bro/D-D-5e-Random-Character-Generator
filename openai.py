#! /usr/bin/env python3

import openai
import argparse

def create_dalle_image(api_key, prompt):
    try:
        # Set the API key
        openai.api_key = api_key

        # Call the DALL-E API
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")

        # The response includes URLs to the generated images
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Generate an image using DALL-E')
    parser.add_argument('api_key', help='OpenAI API key')
    parser.add_argument('prompt', help='Prompt for generating the image')
    args = parser.parse_args()

    # Generate the image
    image_url = create_dalle_image(args.api_key, args.prompt)
    print(image_url)

if __name__ == "__main__":
    main()


    