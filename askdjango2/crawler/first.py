import requests

response  = requests.get('http://askdjango.github.io/lv1/')
html = response.text

print(html)

