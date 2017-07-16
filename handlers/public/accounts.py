import webapp2
from base import BaseHandler

class Accounts(BaseHandler):
    def get(self):
        self.render_template("template/accounts.html")