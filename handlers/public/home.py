import webapp2
import config.settings

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers = {
        #     'x-ibm-client-id': settings.CLIENT_ID,
        #     'x-ibm-client-secret': settings.CLIENT_SECRET,
        #     'accept': "application/json"
        # }
        self.response.write('Hello, World!')

# https://api-uat.unionbankph.com/uhac/sandbox/accounts/{{ACCT_NUM}}