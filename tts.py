from fastapi import FastAPI, WebSocket
from TTS.api import TTS
from scipy.io.wavfile import write as write_wav
import numpy as np
import io

tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

text = "Aman is a very good boy!!"

# 1. Get audio array
wav_array = tts.tts(text)

# 2. Get sample rate separately
sample_rate = tts.synthesizer.output_sample_rate

# 3. Write to buffer
audio_buffer = io.BytesIO()
write_wav(audio_buffer, sample_rate, np.array(wav_array, dtype=np.float32))
audio_buffer.seek(0)

# 4. Debug check
with open("output.wav", "wb") as f:
    f.write(audio_buffer.read())
print("Audio written to output.wav")
