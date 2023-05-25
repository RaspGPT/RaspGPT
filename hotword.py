import os
import sys
import time

sys.path.append()

from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector, MultiHotwordDetector
from eff_word_net.audio_processing import Resnet50_Arc_loss()
from eff_word_net import samples_loc

base_model = Resnet50_Arc_loss()
model_dir = ""

gpt = HotwordDetector(
    hotword = "gpt",
    model = base_model,
    reference_file = os.path.join(model_dir, "gpt_ref.json"),
    threshold = 0.6,
    relaxation_time = 2
)

gpt_yaa = HotwordDetector(
    hotword = "gpt_yaa",
    model = base_model,
    reference_file = os.path.join(model_dir, "gpt_yaa_ref.json"),
    threshold = 0.6,
    relaxation_time = 2
)

multi_hotword_detector = MultiHotwordDetector(
    [gpt, gpt_yaa],
    model = base_model,
    continuous = True
)

def hotword(hotword_stream):
    hotword_stream = SimpleMicStream(window_length_secs=1.5, sliding_window_secs=0.75, mic_stream=hotword_stream)
    hotword_stream.start_stream()

    print("Say GPT or GPT yaa")

    while True:
        frame = hotword_stream.getFrame()
        result = multi_hotword_detector.findBestMatch(frame)

        if(None not in result):
            hotword_stream.close_stream()
            return True