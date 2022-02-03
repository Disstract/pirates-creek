from requests_html import HTMLSession
import time

def ovaGamesSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://www.ovagames.com/?s="+search)

        titles = r.html.find('.post-title a')

        if titles == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(titles)):
                
                results.append(titles[i].text)
                results.append(titles[i].attrs['href'])

        return(results)
    except:
        return("OVA Games: Connection Failed!")
