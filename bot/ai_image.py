import os, openai
openai.api_key = os.environ.get("OPENAI_API_KEY")

async def generate_image(prompt: str):
    resp = openai.Image.create(prompt=prompt, n=1, size="512x512")
    url = resp.data[0].url
    return url
