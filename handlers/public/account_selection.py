import webapp2
from base import BaseHandler

class AccountSelection(BaseHandler):
    def get(self):
        self.render_template("template/acct_selection.html")