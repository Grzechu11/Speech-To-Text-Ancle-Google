from datetime import datetime

from run import api, fields

response_model = api.model('process_audio_response', {
    'processed_date': fields.String(description='Date the file was processed', required=True),
    'file_name': fields.String(description='Name of file', required=True),
    'text': fields.String(description='Predicted text', required=True)
})
    
class ProcessApudioResponse:
    def __init__(self, file_name, full_path):
        self.file_name = file_name
        self.full_path = full_path

        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X") 
        self.processed_date = formatted_now 
        
        self.text = ''

    def set_text(self, text):
        self.text = text

    def ask_uncle_google(self):
        self.set_text('test')