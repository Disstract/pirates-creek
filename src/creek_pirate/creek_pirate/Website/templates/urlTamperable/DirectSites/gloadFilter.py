from requests_html import HTMLSession
import time

def gloadSearch(search):
    results = []
    
    try:
        session = HTMLSession()
        r = session.get("https://gload.to/?s="+search)

        titles = r.html.find('.postsborder a')
        time.sleep(0.05)

        
        if titles == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(titles)):
                
                results.append(titles[i].text)
                results.append(titles[i].attrs['href'])
                
        return(results)
        
    except:
        return("Gload: Connection Failed!")

