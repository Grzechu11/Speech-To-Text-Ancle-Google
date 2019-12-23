from datetime import datetime

from run import api, fields

response_model = api.model('process_audio_response', {
    'processed_date': fields.String(description='Date the file was processed', required=True),
    'file_name': fields.String(description='Name of file', required=True),
    'text': fields.String(description='Predicted text', required=True)
})
    
class ProcessApudioResponse:
  def __init__(self, file_name, text):
    self.file_name = file_name
    self.text = text
          
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X") 
    self.processed_date = formatted_now 