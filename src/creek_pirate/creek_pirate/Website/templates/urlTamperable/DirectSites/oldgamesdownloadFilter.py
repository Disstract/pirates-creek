#post-format-image post-format-wrapper 
from requests_html import HTMLSession
import time
def oldgamesSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://oldgamesdownload.com/?s="+search)

        link = r.html.find('.featured-image')
        time.sleep(0.05)

        if link == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(link)):
                
                results.append(link[i].attrs['href'])
                time.sleep(0.05)
        return(results)
    except:
        results = ["Old Games Download: Connection Failed!"]
        return(results)
