import werkzeug
from flask_restplus import reqparse

file_upload = reqparse.RequestParser()
file_upload.add_argument('audio_file',  
                         type=werkzeug.datastructures.FileStorage, 
                         location='files', 
                         required=True, 
                         help='Audio file')

audio_mimetypes = ['audio/mp3', 'audio/mpeg', 'audio/mp4', 'audio/vnd.wav']