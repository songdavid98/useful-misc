# too lazy to make virtual environment

import json
import ssl
from urllib import request
from urllib.parse import urlencode
from pprint import pprint


def http_request(method, base_url, api_endpoint, body=None, headers=None, context=None):
    url = f"https://{base_url}{api_endpoint}"

    if method.upper() == "GET" and isinstance(body, dict):
        url += ("&" if "?" in url else "?") + urlencode(body)
        body = None
    elif body and isinstance(body, str):
        body = body.encode("utf-8")
    elif body and isinstance(body, dict):
        body = json.dumps(body).encode("utf-8")

    # https://docs.python.org/3/library/urllib.request.html#urllib.request.Request
    req = request.Request(
        url=url,
        data=body,
        headers=headers or {},
        method=method
    )

    try:
        # https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
        with request.urlopen(req, context=context) as response:
            return response.read()
            # result = json.loads(result.decode("utf-8"))
    
    except Exception as e:
        print("Code: ", e.code)
        print("Reason: ", e.reason)
        print(e.read().decode("utf-8"))
        print(e)
        dump_request(req)
    return None

def dump_request(req):
    print(f"URL: {req.full_url}")
    print(f"Method: {req.get_method()}")

    print("\nHeaders:")
    for k, v in req.header_items():
        print(f"  {k}: {v}")

    print("\nData:")
    print(req.data)

# payload = json.dumps({
#     "show_mfa": False,
#     "email": "user@example.com",
#     "password": "secret"
# })

# headers = {
#     "Content-Type": "application/json"
#     #  CloudFlare blocks User-agent: Python-urllib/3.9
#     'User-Agent': 'Python-Client'
# }

# # to ignore ssl cert verification
# context = ssl._create_unverified_context()

# data = http_request(
#     method="POST",
#     base_url="api.example.com",
#     api_endpoint="/login",
#     body=payload,
#     headers=headers,
#     context=context
# )

# if data:
#     response = json.loads(data.decode("utf-8"))
#     print(response["token"])
