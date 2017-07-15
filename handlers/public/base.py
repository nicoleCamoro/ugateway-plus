import os
import jinja2
import webapp2
import json
import logging

# from gaesessions import get_current_session
from models.user import User

# setup template
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname("frontend/")
	),
	autoescape=True
)
JINJA_ENVIRONMENT.globals['uri_for'] = webapp2.uri_for


class BaseHandler(webapp2.RequestHandler):
	def __init__(self, request=None, response=None):
		self.initialize(request, response)

		# self.session = self.get_session()
		# self.user = self.get_current_user()

	# def get_session(self):
	# 	return get_current_session()

	# def get_current_user(self):
	# 	if self.session.has_key("user"):
	# 		user = User.get_by_id(self.session["user"])
	# 		return user
	# 	else:
	# 		return None

	# def login(self, user):
	# 	self.session["user"] = user.key.id()
	# 	return

	# def logout(self):
	# 	if self.session.is_active():
	# 		self.session.terminate()
	# 		return

	def send_json_response(self, response_data):
		self.response.headers["Content-Type"] = "application/json"
		self.response.out.write(json.dumps(response_data))

	def render_template(self, _template, _template_values={}):
		"""Renders a template and writes the result to the response.

		_template: The location of the template
		_template_values: The template values"""
		template = JINJA_ENVIRONMENT.get_template(_template)
		rv = template.render(_template_values)

		try:
		    rv = template.render(_template_values)
		except jinja2.TemplateNotFound:
		    return self.redirect(self.uri_for("error"))

		self.response.write(rv)
