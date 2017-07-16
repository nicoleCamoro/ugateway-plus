import webapp2
from base import BaseHandler

class WithdrawAmount(BaseHandler):
    def get(self):
        self.render_template("template/withdraw-amount.html")