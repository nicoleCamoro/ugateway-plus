import json
import webapp2


class ApiBaseHandler(webapp2.RequestHandler):
	def render(self, data):
		self.response.headers["Content-Type"] = "application/json"
		self.response.write(json.dumps(data))

	@staticmethod
	def construct_response_details(code, status, payload=None, message=None):
		"""Constructs a response details object.

		status: The HTTP status code
		code: The custom code for additional identification of response status
		message: The descriptive message of the response status
		return: The response details object"""
		details = {}
		details["status"] = status
		details["code"] = code

		if payload:
			details["payload"] = payload

		if message:
			details["message"] = message

		return details
