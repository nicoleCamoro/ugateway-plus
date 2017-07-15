import webapp2
import config.settings
from base import BaseHandler

class MainPage(BaseHandler):
    def get(self):
        # self.response.headers = {
        #     'x-ibm-client-id': settings.CLIENT_ID,
        #     'x-ibm-client-secret': settings.CLIENT_SECRET,
        #     'accept': "application/json"
        # }
        self.render_template("template/index.html")

# https://api-uat.unionbankph.com/uhac/sandbox/accounts/{{ACCT_NUM}}