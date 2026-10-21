# made this because i was too lazy to create a virtual environment

import http.client
import json
import urllib.parse
import ssl

from pprint import pprint


# how to make a payload:
# payload = json.dumps({
#     "show_mfa": False,
#     "email": self.bp_email,
#     "password": self.bp_password
# })

# how to make headers:
# headers = {
#     'Content-Type': 'application/json'
# }


def http_request( method, base_url, api_endpoint, body, headers, context=None ):
	conn = http.client.HTTPSConnection( base_url, context=context )
	# https://docs.python.org/3/library/http.client.html#httpconnection-objects
	conn.request(
		method=method,
		url=api_endpoint,
		body=body,
		headers=headers
    )
	response = ''
	try:
		response = conn.getresponse()
		# https://docs.python.org/3/library/http.client.html#httpresponse-objects
	except Exception as e:
		print(e)
	if not (200 <= response.status < 300):
		print("Something went wrong with the request")
		print( response, response.status, response.reason )
		pprint( response.read() )
		return
	data = response.read()
	conn.close()
	return data                 # print( data["token"] )


# url_params = {'test' : 'test'}
# server = 'test.org'
# endpoint = '/api/test?' + urllib.parse.urlencode(url_params)
# # some routes end with a '/', so also check '/api/test/?'
# # body = None
# body = json.dumps({
# 	"test": "test",  
# })
# # headers = {}
# headers = {
#     'Content-Type': 'application/json'
# }
# # to ignore ssl cert verification
# context = ssl._create_unverified_context()
# result = http_request('POST', server, endpoint, body, headers, context)
# pprint( result )
