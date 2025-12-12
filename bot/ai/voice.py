import os, openai, asyncio

openai.api_key = os.environ.get("OPENAI_API_KEY")

async def transcribe_voice(path: str):
    def sync_transcribe():
        with open(path, "rb") as f:
            return openai.Audio.transcriptions.create(file=f, model="whisper-1").text
    return await asyncio.to_thread(sync_transcribe)
