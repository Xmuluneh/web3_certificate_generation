#!/usr/bin/python3
import openai 
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('API_KEY')

try:
    response = openai.Image.create(
        prompt='Students Certification',
        n=1,
        size='1024x1024'
    )
    image_url = response['data'][0]['url']
    print(image_url)
except Exception as e:
    print(f"Error: {e}")