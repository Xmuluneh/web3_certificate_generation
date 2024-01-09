#!/usr/bin/python3
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('API_KEY')
response = OpenAI.Image.create(
  prompt = 'yellow sport car',
  n =1,
  size = '1024x1024'
)
image_url = response['data'][0]['url']
print(image_url)