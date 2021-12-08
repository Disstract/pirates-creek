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

        if titles == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(titles)):
                
                results.append(titles[i].text)
                results.append("https://gog-games.com"+link[i].attrs['href'])
                time.sleep(0.05)
        return(results)
    except:
        return("GOG Games: Connection Failed!")