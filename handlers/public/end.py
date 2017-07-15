import webapp2
from base import BaseHandler

class End(BaseHandler):
    def get(self):
        self.render_template("template/end.html")