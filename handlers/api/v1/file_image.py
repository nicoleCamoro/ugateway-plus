from handlers.api.v1.base import ApiBaseHandler
# from models.user import User
from libraries.helpers import functions
import logging

class FileHandler(ApiBaseHandler):

    def post(self):
        """ Post to User """

        user_inputs = self.request.POST.items()
        props = functions.convert_key_val_pairs(user_inputs)
        
        
        # user = User.save(props)

        # user_json = User.to_dict(user.get())
        response = self.construct_response_details(
            200, "Ok!", props)

        self.render(response)
