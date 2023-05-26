import pyaudio
import time
import wave
import json

with open("./conf.json", 'r') as f:
    conf = json.load(f)

def get_ques(ques_stream, pa):

    ques_stream.start_stream()

    frames = []

    time.sleep(0.5)
    print("start")
    start = time.time()

    while time.time() - start < conf.Q_RANGE:
        data = ques_stream.read(conf.Q_CHUNK, exception_on_overflow = False)
        frames.append(data)

    ques_stream.stop_stream()

    f_byte = b''.join(frames)

    wf = wave.open("output.wav", "wb")
    wf.setnchannels(conf.CHANNELS)
    wf.setsampwidth(pa.get_sample_size(conf.FORMAT))
    wf.setframerate(conf.RATE)
    wf.writeframes(f_byte)
    wf.close()