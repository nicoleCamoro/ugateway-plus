import sys
import webapp2
from webapp2_extras import routes

# Public
from handlers.public.home import MainPage
from handlers.public.face_detect import FaceDetection
from handlers.public.success import Success
from handlers.public.end import End
from handlers.public.select_account import AcctSelection
from handlers.public.menu import Menu

# API
from handlers.api.v1.user import UserHandler
from handlers.api.v1.file_image import FileHandler
from handlers.api.v1.enroll import EnrollHandler

app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=MainPage, name='www-main'),
        webapp2.Route('/facial_recognition', handler=FaceDetection, name='www-face-detection'),
        webapp2.Route('/acct_selection', handler=AcctSelection, name='www-acct-selection'),
        webapp2.Route('/menu', handler=Menu, name='www-acct-selection'),
        webapp2.Route('/login', handler=Success, name='www-login'),
        webapp2.Route('/logout', handler=End, name='www-logout'),

        # API
        webapp2.Route('/api/v1/user', handler=UserHandler, name='api-user'),
        webapp2.Route('/api/v1/upload', handler=FileHandler, name='api-file'),
        webapp2.Route('/api/v1/enroll', handler=EnrollHandler, name='api-file'),
    ])
])
