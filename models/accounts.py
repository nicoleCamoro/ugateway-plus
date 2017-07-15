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

    @classmethod
    def to_dict(ndb_props):

        return {
            "id": ndb_props.key.url_safe(),
            "acct_name": ndb_props.acct_name,
            "acct_type": ndb_props.acct_type,
        }
