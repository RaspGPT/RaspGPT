from hotword import *
from audio_prompt import *
from google_stt_tts.google_stt import *

import time
import pyaudio

p = pyaudio.PyAudio()

class MicStream:
    def __init__(self, frames_p):
        self.mic_stream = p.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = 16000,
            input = True,
            frames_per_buffer = frames_p,
            input_device_index = 1
        )

        self.mic_stream.start_stream()

    def _close(self):
        self.mic_stream.stop_stream()
        self.mic_stream.close()

mic = MicStream(12000)
mic_stream = mic.mic_stream

while True:
    if hotword_detection(mic_stream):
        mic._close()
        
        time.sleep(1)
        
        mic = MicStream(1024)
        mic_stream = mic.mic_stream
        get_ques(mic_stream, p)
        question = stt()
        print(question)


    time.sleep(1)

mic._close()
q.terminate()