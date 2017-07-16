import webapp2
from base import BaseHandler

class LogScreen(BaseHandler):
    def get(self):
        self.render_template("template/logscreen.html")