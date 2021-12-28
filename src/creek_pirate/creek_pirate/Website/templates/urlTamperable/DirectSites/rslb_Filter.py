from requests.sessions import session
from requests_html import HTMLSession

def rslbSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://search.rlsbb.ru/?s="+search)

        titles = r.html.find('a', first=True)
        print(titles.text)
        

    except:
        return("RSLB Connection Failed!")

print(rslbSearch(input("Enter ")))
