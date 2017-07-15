import webapp2
from base import BaseHandler

class AcctSelection(BaseHandler):
    def get(self):
        self.render_template("templates/acct_selection.html")