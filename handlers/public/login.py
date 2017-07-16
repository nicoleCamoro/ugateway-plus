import webapp2
from base import BaseHandler
class Login(BaseHandler):
    def get(self):
        self.render_template("template/login.html")