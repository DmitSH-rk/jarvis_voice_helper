import vosk
import sys
import sounddevice as sd
import queue
import json
import time

model = vosk.Model("model_small")
samplerate = 16000
device = 1

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                        channels=1, callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):

                callback(json.loads(rec.Result())["text"])

# def va_listen_with_delay(callback, delay=3):
#     while True:
#         if q.empty() == False:
#             False
#         else:    
#             time.sleep(0.1)  # Маленькая задержка перед повторной проверкой
#     time.sleep(2)
#     va_listen(callback)

def va_listen_once(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                        channels=1, callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        data = q.get()
        if rec.AcceptWaveform(data):
            callback(json.loads(rec.Result())["text"])