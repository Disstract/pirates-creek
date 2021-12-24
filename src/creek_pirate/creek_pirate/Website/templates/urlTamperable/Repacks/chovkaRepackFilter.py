from requests_html import HTMLSession
import time

def chovkaSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://repack.info/search/"+search)

        titles = r.html.find('.title')
        link = r.html.find('.text-dark')

        for i in range(0, len(titles)):
            results.append(titles[i].text)
            try:
                results.append(link[i].attrs['href'])
            except:
                pass
        if results == []:
            results.append("Nothing Found")
        return(results)
    except:
        return("Chovka Repacks: Connection Failed!")