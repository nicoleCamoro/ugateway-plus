from handlers.api.v1.base import ApiBaseHandler
# from models.user import User
from libraries.helpers import functions
from libraries import kairos_face
from models.image import Image

class FileHandler(ApiBaseHandler):

    def post(self):
        """ Post to User """

        user_inputs = self.request.POST.get('logo')
        file_obj = functions.gcs_upload(user_inputs)

        file_info = Image.save(file_obj)
        file_json = Image.to_dict(file_info)

        response = self.construct_response_details(
            200, "Ok!", file_json)

        self.render(response)
