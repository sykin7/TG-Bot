import os
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")

async def gpt_reply(message: str):
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":message}],
        max_tokens=500
    )
    return resp.choices[0].message.content
