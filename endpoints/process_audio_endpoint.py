
from endpoints.models.process_audio_response import response_model, ProcessApudioResponse
import os
import werkzeug
import endpoints.parsers as parsers
from run import app, api, Resource, request, fields, abort, reqparse

UPLOAD_DIRECTORY = "api_uploaded_files"

ns = api.namespace('ProcessAudio',
                   description='Process audio file')


@ns.route('/<file_id>')
class ProcessAudioEndpoint(Resource):
    @ns.expect(parsers.file_upload)
    @ns.marshal_with(response_model, mask=False, code=200)
    def post(self, file_id):
        if "/" in file_id:
            abort(400, 'no subdirectories directories allowed')

        args = parsers.file_upload.parse_args()
        audio_file = args['audio_file']
        if audio_file is None:
            abort(400, 'file not found in request')

        if audio_file.mimetype not in parsers.audio_mimetypes:
            abort(400, 'file mimetype is not audio')

        destination = os.path.join(UPLOAD_DIRECTORY)
        if not os.path.exists(destination):
            os.makedirs(destination)

        audio_file_path = os.path.join(
            destination, '%s_%s' % (file_id, audio_file.filename))
        audio_file.save(audio_file_path)

        return ProcessApudioResponse(audio_file_path, 'text')
