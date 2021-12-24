from requests.sessions import session
from requests_html import HTMLSession
import time

# Search
def crackhubSearch(search):
    results = []
    try:
         
        session = HTMLSession()
        r = session.get("https://crackhub.site/?s="+search)

        titles = r.html.find('.entry-title')
        try:
            link = r.html.find('.entry-title a')
        except:
            pass

        for i in range(0, len(titles)):
            results.append(titles[i].text)
            try:
                results.append(link[i].attrs['href'])
            except:
                pass
        if results == []:
            results.append("Nothing Found")
        return(results)
    except:
        return("Crackhub: Connection Failed!")


