# Smart Speaker using chatGPT API

## Demo Video
https://github.com/RaspGPT/RaspGPT/assets/29935114/ad68328d-6b52-431f-ae98-c326d5f3b031

## Env
- Raspberry Pi 3b+
- Raspberry Pi OS (64-bit)

## Architecture
![flow](https://github.com/RaspGPT/RaspGPT/assets/29935114/15a49f90-4899-4dfd-8a17-cf4203a7dfda)
### Feature
 - hotword detection
 - speech to text
 - text to speech
 - using chatGPT

## Requirements
- python3.8.16
- pyaudio
- EfficientWord-Net
  - tflite-runtime
  - llvmlite 0.36.0
  - numpy 1.20.0
  - numba 0.51.2
  - librosa 0.8.1
- pygame
- google_cloud_speech
- google_cloud_texttospeech

### TODO
- hotword - end option
- change `time.sleep()`
- improve stability (try-except)
