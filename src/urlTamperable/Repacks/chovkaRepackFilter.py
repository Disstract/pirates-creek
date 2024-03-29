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
        
        results = zip(results[::2], results[1::2])
        return(results)
    except:
        results = ["Chovka Repacks: Connection Failed!"]
        return(results)
