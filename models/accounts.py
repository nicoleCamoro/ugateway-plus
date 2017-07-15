from google.appengine.ext import ndb


class Account(ndb.Model):
    acct_name = ndb.StringProperty()
    acct_type = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def save(cls, property_values):
        acct = cls()

        if property_values["acct_name"]:
            acct.acct_name = property_values["acct_name"]
        if property_values["acct_type"]:
            acct.acct_type = property_values["acct_type"]

        return acct.put()