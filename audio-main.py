## Packages
from vosk import Model, KaldiRecognizer
import wave
import json
import os
import pyaudio
import tempfile
import time

## Class > Functions
class AUDIO:
    def __init__(self):
        try:
            self.model_path = "Models/vosk-model-en-us-0.22"
            self.model = Model(self.model_path)
        except Exception as error:
            print(error)
    
    def transcribeAudio(self, audio_file_path):
        with wave.open(audio_file_path, "rb") as wf:
            if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
                print("Audio file must be WAV format mono PCM.")
                return

            recognizer = KaldiRecognizer(self.model, wf.getframerate())

            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    return json.loads(result)["text"]

            final_result = recognizer.FinalResult()
            return json.loads(final_result)["text"]

    def recordAudio(self, duration, sample_rate=16000):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=1024)

        print("Listening...")
        frames = []
        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        print("Processed...")
        stream.stop_stream()
        stream.close()
        p.terminate()

        temp_dir = tempfile.gettempdir()
        audio_file_path = os.path.join(temp_dir, "temp_audio.wav")
        with wave.open(audio_file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

        return audio_file_path

    def audioCapture(self, duration: int = 5) -> any:
        audio_file_path = self.recordAudio(duration)
        return self.transcribeAudio(audio_file_path)

    def recognizeSpeech(self):
        try:
            speech_text = str(self.audioCapture(5))
            if speech_text.strip():
                return speech_text
            else:
                print("No speech detected.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.1)

## Main Code
if __name__ == "__main__":
    audio = AUDIO()
    while True:
        result = audio.recognizeSpeech()
        print(f"You said: {result}")