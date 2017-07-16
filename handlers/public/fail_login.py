import webapp2
from base import BaseHandler

class FailLogin(BaseHandler):
    def get(self):
        self.render_template("template/fail-login.html")