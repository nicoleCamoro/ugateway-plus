import webapp2
from base import BaseHandler

class ErrNotRecognized(BaseHandler):
    def get(self):
        self.render_template("template/verify-error-notrecognize.html")