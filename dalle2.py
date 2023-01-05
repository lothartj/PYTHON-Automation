import openai
import os

openai.api_key = "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"

response = openai.Image.create(
    prompt='a kid in jupiter',
    n=1,
    size='1024x1024'
)
image_url = response['data'][0]['url']
print(image_url)