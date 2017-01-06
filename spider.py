import requests
from consts import const

req = requests.get(const.API_STAT)
print(req.content)
