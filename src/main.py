import numpy 
import requests

r = requests.get("http://comic.naver.com")

print(r.content) 


