#https://archive.org/search.php?query=descent
from requests_html import HTMLSession
import time

def myabandonwareSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://www.myabandonware.com/search/q/"+search)

        titles = r.html.find('.name')
        link = r.html.find('.name')

        if titles == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(titles)):
                
                results.append(titles[i].text)
                results.append("https://www.myabandonware.com/game"+link[i].attrs['href'])
                time.sleep(0.05)
        return(results)
    except:
        results = ["My Abandonware: Connection Failed!"]
        return(results)
