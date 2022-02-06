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
        link = r.html.find('.entry-title a')

        for i in range(0, len(titles)):
            try:
                results.append(titles[i].text)
                results.append(link[i].attrs['href'])
            except:
                pass
        if results == []:
            results.append("Nothing Found")

        results = zip(results[::2], results[1::2])
        return(results)
    except:
        results = ["Crackhub Scene: Connection Failed!"]
        return(results)

