import webapp2
from base import BaseHandler

class SMSpass(BaseHandler):
    def get(self):
        self.render_template("template/verify-smspasscode.html")