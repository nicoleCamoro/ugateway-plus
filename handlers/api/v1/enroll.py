from handlers.api.v1.base import ApiBaseHandler
# from models.user import User
from libraries.helpers import functions
from libraries import kairos_face
from models.image import Image

class EnrollHandler(ApiBaseHandler):

    def post(self):
        """ Post to User """

        user_inputs = self.request.POST.get('image')
        analysis = kairos_face.enroll_face(url=user_inputs, subject_id='franchette', gallery_name='a-gallery')

        response = self.construct_response_details(
            200, "Ok!", "Success")

        self.render(response)

