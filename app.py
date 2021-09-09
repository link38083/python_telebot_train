import requests
import ipinfo

access_token = '3c805bd8202418'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()
#r = requests.get("http://ipinfo.io/city?Content?token=3c805bd8202418")
print(details.city)