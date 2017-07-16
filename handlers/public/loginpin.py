import webapp2
from base import BaseHandler

class LoginPin(BaseHandler):
    def get(self):
        self.render_template("template/LoginPin.html")