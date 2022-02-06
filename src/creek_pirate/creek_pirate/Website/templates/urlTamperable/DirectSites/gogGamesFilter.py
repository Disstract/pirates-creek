#https://gog-games.com/search/enter
from requests_html import HTMLSession
import time

def gogGamesSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://gog-games.com/search/"+search)

        titles = r.html.find('.title')
        link = r.html.find('.block')
        for i in range (0, len(titles)):
            try:
                results.append(titles[i].text)
                results.append("https://gog-games.com"+link[i].attrs['href'])
            except:
                pass

        if titles == []:
            results.append("Nothing Found")

        results = zip(results[::2], results[1::2])
        return(results)
    except:
        results = ["GOG Games: Connection Failed!"]
        return(results)
