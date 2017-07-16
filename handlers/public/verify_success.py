import webapp2
from base import BaseHandler

class VerifySuccess(BaseHandler):
    def get(self):
        self.render_template("template/verify-success.html")