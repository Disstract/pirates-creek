#https://www.macbed.com/?s=
from requests.sessions import session
from requests_html import HTMLSession

def macbedSearch(search):
    results = []
    
     session = HTMLSession()
    
