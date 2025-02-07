import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'aidar'
put_accent = True
put_yo = True

device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id,
                                     trust_repo=True)

model.to(device)  # gpu or cpu

def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()