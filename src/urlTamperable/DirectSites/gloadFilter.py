from requests_html import HTMLSession
import time

def gloadSearch(search):
    results = []
    
    try:
        session = HTMLSession()
        r = session.get("https://gload.to/?s="+search)

        titles = r.html.find('.postsborder a')
        time.sleep(0.05)

        for i in range (0, len(titles)):
            try:
                results.append(titles[i].text)
                results.append(titles[i].attrs['href'])
            except:
                pass
        if titles == []:
            results.append("Nothing Found")

        results = zip(results[::2], results[1::2])
        return(results)
        
    except:
        return("Gload: Connection Failed!")

