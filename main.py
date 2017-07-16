import sys
import webapp2
from webapp2_extras import routes

# Public
from handlers.public.account_selection import AccountSelection
from handlers.public.accounts import Accounts
from handlers.public.end import End
from handlers.public.face_detect import FaceDetection
from handlers.public.fail_login import FailLogin
from handlers.public.home import MainPage
from handlers.public.login import Login
from handlers.public.loginpin import LoginPin
from handlers.public.logscreen import LogScreen
from handlers.public.mainscreen import MainScreen
from handlers.public.menu import Menu
from handlers.public.success import Success
# from handlers.public.verify_image import 
from handlers.public.verify_error_notrecognize import ErrNotRecognized
from handlers.public.verify_smspasscode import SMSpass
from handlers.public.verify_success import VerifySuccess
from handlers.public.verifyingface import VerifyFace
from handlers.public.withdraw_amount import WithdrawAmount
from handlers.public.withdraw import Withdraw

# API
from handlers.api.v1.user import UserHandler
from handlers.api.v1.file_image import FileHandler
from handlers.api.v1.enroll import EnrollHandler

app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=MainPage, name='www-main'),
        webapp2.Route('/accounts', handler=Accounts, name=''),
        webapp2.Route('/acct_selection', handler=AccountSelection, name=''),
        webapp2.Route('/end', handler=End, name=''),
        webapp2.Route('/face_detect', handler=FaceDetection, name=''),
        webapp2.Route('/fail-login', handler=FailLogin, name=''),
        webapp2.Route('/login', handler=Login, name=''),
        webapp2.Route('/loginpin', handler=LoginPin, name=''),
        webapp2.Route('/logscreen', handler=LogScreen, name=''),
        webapp2.Route('/mainscreen', handler=MainScreen, name=''),
        webapp2.Route('/menu', handler=Menu, name=''),
        webapp2.Route('/success', handler=Success, name=''),
        webapp2.Route('/verify-error-notrecognize', handler=ErrNotRecognized, name=''),
        webapp2.Route('/verify-smspasscode', handler=SMSpass, name=''),
        webapp2.Route('/verify-success', handler=VerifySuccess, name=''),
        webapp2.Route('/verifiyingface', handler=VerifyFace, name=''),
        webapp2.Route('/withdraw-amount', handler=WithdrawAmount, name=''),
        webapp2.Route('/withdraw', handler=Withdraw, name=''),

        # API
        webapp2.Route('/api/v1/user', handler=UserHandler, name='api-user'),
        webapp2.Route('/api/v1/upload', handler=FileHandler, name='api-file'),
        webapp2.Route('/api/v1/enroll', handler=EnrollHandler, name='api-file'),
    ])
])
