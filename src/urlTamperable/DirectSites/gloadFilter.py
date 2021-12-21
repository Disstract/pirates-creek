from requests_html import HTMLSession
import time

def gloadSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://gload.to/?s="+search)

        link = r.html.find('.postsborder a')
        if link == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(link)):
                try:
                    results.append(link[i].attrs['href'])
                except:
                    pass
        return(results)
        
    except:
        return("Gload: Connection Failed!")
    
