from google.appengine.ext import ndb


class User(ndb.Model):
    """ User model """

    email = ndb.StringProperty()
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    pin = ndb.StringProperty()
    balance = ndb.FloatProperty()
    account_num = ndb.IntegerProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def save(cls, property_values):

        user = cls()

        if property_values["email"]:
            user.email = property_values["email"]
        if property_values["firstname"]:
            user.firstname = property_values["firstname"]
        if property_values["lastname"]:
            user.lastname = property_values["lastname"]
        if property_values["balance"]:
            user.balance = property_values["balance"]
        if property_values["pin"]:
            user.pin = property_values["pin"]
        return user.put()

    @classmethod
    def to_dict(ndb_props):

        return {
            "id": ndb_props.key.url_safe(),
            "email": ndb_props.email,
            "firstname": ndb_props.firstname,
            "lastname": ndb_props.lastname,
            "balance": ndb_props.balance,
            "pin": ndb_props.pin
        }
