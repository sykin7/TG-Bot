import openai, os
openai.api_key = os.environ.get("OPENAI_API_KEY")

async def transcribe_voice(path: str):
    audio_file = open(path, "rb")
    transcript = openai.Audio.transcriptions.create(file=audio_file, model="whisper-1")
    return transcript.text
