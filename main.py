import sys
import webapp2
from webapp2_extras import routes

# Public
from handlers.public.home import MainPage
from handlers.public.face_detect import FaceDetection

# API
from handlers.api.v1.user import UserHandler

app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=MainPage, name='www-main'),
        webapp2.Route('/facial_recognition', handler=FaceDetection, name='www-face-detection'),
        webapp2.Route('/login', handler=FaceDetection, name='www-login'),
        webapp2.Route('/logout', handler=FaceDetection, name='www-logout'),

        # API
        webapp2.Route('/api/v1/user', handler=UserHandler, name='api-user'),
    ])
])
