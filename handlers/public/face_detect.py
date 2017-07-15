import webapp2
from base import BaseHandler
class FaceDetection(BaseHandler):
    def get(self):
        self.render_template("templates/face_detect.html")