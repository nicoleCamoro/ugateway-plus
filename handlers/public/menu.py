import webapp2
from base import BaseHandler

class Menu(BaseHandler):
    def get(self):
        self.render_template("templates/menu.html")