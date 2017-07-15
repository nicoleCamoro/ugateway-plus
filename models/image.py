from google.appengine.ext import ndb


class Image(ndb.Model):

    blob_key = ndb.StringProperty()
    image_url = ndb.StringProperty()
    public_url = ndb.StringProperty()
    filename = ndb.StringProperty()

    @classmethod
    def save(cls, property_values):

        image = cls()

        if property_values["blob_key"]:
            image.blob_key = property_values["blob_key"]
        if property_values["image_url"]:
            image.image_url = property_values["image_url"]
        if property_values["public_url"]:
            image.public_url = property_values["public_url"]
        if property_values["filename"]:
            image.filename = property_values["filename"]
        return image.put()