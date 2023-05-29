from hotword import *
from audio_prompt import *
from google_stt_tts.convert_core import *
import json

import time
import pyaudio

p = pyaudio.PyAudio()

with open("./conf.json", 'r') as f:
    conf = json.load(f)

class MicStream:
    def __init__(self, frames_p):
        self.mic_stream = p.open(
            format = conf.FORMAT,
            channels = conf.CHANNELS,
            rate = conf.RATE,
            input = True,
            frames_per_buffer = frames_p,
            input_device_index = conf.INPUT_DEVICE_INDEX
        )

        self.mic_stream.start_stream()

    def _close(self):
        self.mic_stream.stop_stream()
        self.mic_stream.close()

mic = MicStream(conf.H_CHUNK)
mic_stream = mic.mic_stream

g_stt_tts = GoogleConvert()

while True:
    if hotword_detection(mic_stream):
        mic._close()
        
        time.sleep(1)
        
        mic = MicStream(conf.Q_CHUNK)
        mic_stream = mic.mic_stream
        get_ques(mic_stream, p)
        question = g_stt_tts.stt()
        print(question)

        mic._close()
        time.sleep(0.5)
        mic = MicStream(conf.H_CHUNK)
        mic_stream = mic.mic_stream

        g_stt_tts.tts(question)

    time.sleep(1)

mic._close()
q.terminate()