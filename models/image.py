from google.appengine.ext import ndb


class Image(ndb.Model):

    gs_key = ndb.StringProperty()
    gcs_filename = ndb.StringProperty()
    serving_url = ndb.StringProperty()
    public_url = ndb.StringProperty()
    filename = ndb.StringProperty()
    filetype = ndb.StringProperty()

    @classmethod
    def save(cls, property_values):

        image = cls()

        if property_values["gs_key"]:
            image.gs_key = property_values["gs_key"]
        if property_values["gcs_filename"]:
            image.gcs_filename = property_values["gcs_filename"]
        if property_values["serving_url"]:
            image.serving_url = property_values["serving_url"]
        if property_values["public_url"]:
            image.public_url = property_values["public_url"]
        if property_values["filename"]:
            image.filename = property_values["filename"]
        if property_values["filetype"]:
            image.filetype = property_values["filetype"]
        return image.put()

    @classmethod
    def to_dict(cls, ndb_props):

        data = {
            "id": ndb_props.key.urlsafe(),
            "gs_key": ndb_props.gs_key,
            "gcs_filename": ndb_props.gcs_filename,
            "serving_url": ndb_props.serving_url,
            "public_url": ndb_props.public_url,
            "filename": ndb_props.filename,
            "filetype": ndb_props.filetype,
        }

        return data