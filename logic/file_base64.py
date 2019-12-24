# Import the base64 encoding library.
import base64

# Pass the audio data to an encoding function.
def encode_audio(sound_file):
    fin = open(sound_file, "rb")
    binary_data = fin.read()
    fin.close()
    b64_data = base64.b64encode(binary_data)
    print(b64_data)
    return b64_data


encode_audio('./api_uploaded_files/1_nowy dzien.mp3')