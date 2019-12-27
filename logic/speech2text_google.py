import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

credential_path = "./keys/SpeechToText-google.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    
class GoogleSpeechToText:
    def __init__(self, full_path):
        self.full_path = full_path        
        self.text = ''

    def set_text(self, text):
        self.text = text

    def ask_uncle_google(self):
        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        # file_name = os.path.join(
        #     os.path.dirname(__file__),
        #     'api_uploaded_files',
        #     '1_nowy dzien.mp3')
        
        # Loads the audio into memory
        with io.open(self.full_path, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
            sample_rate_hertz=16000,
            language_code='pl-PL')

        # Detects speech in the audio file
        response = client.recognize(config, audio)

        transcripts = []
        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))
            transcripts.append(result.alternatives[0].transcript)

        return ','.join(transcripts)