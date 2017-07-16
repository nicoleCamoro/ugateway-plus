import webapp2
from base import BaseHandler

class Withdraw(BaseHandler):
    def get(self):
        self.render_template("template/withdraw.html")