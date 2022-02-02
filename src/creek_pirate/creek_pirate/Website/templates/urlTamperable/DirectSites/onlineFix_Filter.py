from requests.sessions import session
from requests_html import HTMLSession


def onlineFixSearch(search):
    results = []
    
    try:
        session = HTMLSession()
        r = session.get("https://online-fix.me/index.php?do=search&subaction=search&story="+search)
        
        titles =  r.html.find('.title', first = True)
        return(titles.text)

    except:
        results = ["Crackhub Scene: Connection Failed!"]
        return(results)



search = input("enter ")
print(onlineFixSearch(search))


