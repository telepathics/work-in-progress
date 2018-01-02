import sys
sys.dont_write_bytecode = True

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
from functions import *

class Handler(BaseHTTPRequestHandler):

	def end_headers(self):
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Access-Control-Allow-Headers", "Content-Type, Content-Length")
		self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
		self.send_header("Access-Control-Allow-Credentials", "true")
		BaseHTTPRequestHandler.end_headers(self)

	def handleError(self, status_code, error):
		self.send_response(status_code)
		self.send_header("Content-Type", "text/plain")
		self.end_headers()
		self.wfile.write(error.encode("utf-8"))

	def checkPath(self, mask):
		mask_parts = mask[1:].split("/")
		path_parts = self.path[1:].rstrip("/").split("/")
		if len(mask_parts) != len(path_parts):
			self.url_vars = {}
			return False

		vars = {}
		for i in range(len(mask_parts)):
			if mask_parts[i][0] == "{":
				vars[mask_parts[i][1:-1]] = path_parts[i]
			else:
				if mask_parts[i] != path_parts[i]:
					self.url_vars = {}
					return False

		self.url_vars = vars
		return True

	def do_OPTIONS(self):
		self.send_response(200)
		self.end_headers()


def main():
	listen = ("127.0.0.1", 8080)
	server = HTTPServer(listen, Handler)

	print("Listening...")
	server.serve_forever()

main()
