import sys
import webapp2
from webapp2_extras import routes

# Public
from handlers.public.home import MainPage


app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=MainPage, name='www-main'),
    ])
])
