import webapp2
from base import BaseHandler

class MainScreen(BaseHandler):
    def get(self):
        self.render_template("template/mainscreen.html")