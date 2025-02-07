# voice-recognition

### Overview
This project provides a Python-based audio transcription system using the Vosk speech recognition library. It records audio, processes it, and converts speech into text using a pre-trained Vosk model. To download the vosk model file, follow this instructions:
- Visit [official vosk github models page](https://github.com/alphacep/vosk-space/blob/master/models.md)
- Modify the audio-main.py file, especially the `self.model_path`:
```python
## Class > Functions
class AUDIO:
    def __init__(self):
        try:
            self.model_path = "Models/vosk-model-en-us-0.22" ## change this with whatever 'vosk model' you have inside the models folder.
            self.model = Model(self.model_path)
        except Exception as error:
            print(error)
```

### Features
- **Audio Recording**: Captures live audio input using PyAudio.
- **Speech Recognition**: Uses Vosk's KaldiRecognizer to transcribe spoken words into text.
- **Temporary File Management**: Saves recorded audio as a temporary WAV file for processing.
- **Real-Time Speech Detection**: Recognizes speech in real-time and provides output.

### Dependencies
- `vosk`
- `pyaudio`
- `wave`
- `json`
- `os`
- `tempfile`
- `time`

### Usage
1. Install the required dependencies using `pip install vosk pyaudio`.
2. Place the Vosk model in the `Models/` directory.
3. Run the script: `python script_name.py`.
4. Speak into the microphone, and the system will transcribe your speech in real-time.

### Code Structure
- **AUDIO Class**
  - `transcribeAudio(audio_file_path)`: Converts an audio file into text.
  - `recordAudio(duration, sample_rate)`: Records audio for a given duration.
  - `audioCapture(duration)`: Captures and transcribes speech.
  - `recognizeSpeech()`: Continuously listens and transcribes speech.
- **Main Execution**
  - Creates an instance of `AUDIO` and loops to recognize speech.


## How to modify:
### Recording Duration
As you can see, there's a ``duration`` variable inside the `audioCapture` function, change it to your likings. The default is 5 seconds recording, and then wait for it to proccess the given audio/data.
```python
    def audioCapture(self, duration: int = 5) -> any:
        audio_file_path = self.recordAudio(duration)
        return self.transcribeAudio(audio_file_path)
```
