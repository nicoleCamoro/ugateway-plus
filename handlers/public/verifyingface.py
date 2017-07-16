import webapp2
from base import BaseHandler

class VerifyFace(BaseHandler):
    def get(self):
        self.render_template("template/verifyingface.html")