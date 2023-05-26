import pyaudio
import time
import wave

def get_ques(ques_stream, pa):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    ques_stream.start_stream()

    frames = []
    time_limit = 5

    time.sleep(0.5)
    print("start")
    start = time.time()

    while time.time() - start < time_limit:
        data = ques_stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)

    ques_stream.stop_stream()

    f_byte = b''.join(frames)

    wf = wave.open("output.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(f_byte)
    wf.close()