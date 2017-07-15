import webapp2
from base import BaseHandler

class Success(BaseHandler):
    def get(self):
        self.render_template("templates/success.html")