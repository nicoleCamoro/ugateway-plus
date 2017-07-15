from google.appengine.datastore.datastore_query import Cursor

from handlers.api.v1.base import ApiBaseHandler
from models.user import User
import logging

class UserHandler(ApiBaseHandler):

    def post(self):
        """ Post to User """

        user_inputs = self.request.POST.items()

        logging.debug(user_inputs)

        # user = User.create({
        #     "email": props["email"],
        # })

        # send email on successful POST with acct info
        # user_json = User.to_dict(user.get())
        response = self.construct_response_details(
            200, "Ok!", user_inputs)

        self.render(response)
