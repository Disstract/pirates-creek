from requests_html import HTMLSession
import time

def ovaGamesSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://www.ovagames.com/?s="+search)

        titles = r.html.find('.post-title a')

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
        return("OVA Games: Connection Failed!")
