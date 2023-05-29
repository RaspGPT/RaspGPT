import os
import sys
import time

import json
with open("./conf.json", 'r') as f:
    conf = json.load(f)

sys.path.append(conf.EFFWORDNET_PATH)

from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector, MultiHotwordDetector
from eff_word_net.audio_processing import Resnet50_Arc_loss

base_model = Resnet50_Arc_loss()
model_dir = conf.MODEL_PATH
ans_wav_path = "./ans.wav"

gpt = HotwordDetector(
    hotword = "gpt",
    model = base_model,
    reference_file = os.path.join(model_dir, "gpt_ref.json"),
    threshold = conf.H_THRESHOLD,
    relaxation_time = conf.H_RELAXATION_TIME
)

gpt_yaa = HotwordDetector(
    hotword = "gpt_yaa",
    model = base_model,
    reference_file = os.path.join(model_dir, "gpt_yaa_ref.json"),
    threshold = conf.H_THRESHOLD,
    relaxation_time = conf.H_RELAXATION_TIME
)

multi_hotword_detector = MultiHotwordDetector(
    [gpt, gpt_yaa],
    model = base_model,
    continuous = True
)

def hotword_detection(hotword_stream):
    hotword_stream = SimpleMicStream(window_length_secs=1.5, sliding_window_secs=0.75, mic_stream=hotword_stream)
    hotword_stream.start_stream()

    print("Say GPT or GPT yaa")

    while True:
        frame = hotword_stream.getFrame()
        result = multi_hotword_detector.findBestMatch(frame)

        if(None not in result):
            os.system('aplay '+ans_wav_path)
            hotword_stream.close_stream()
            return True