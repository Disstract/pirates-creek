#https://archive.org/search.php?query=descent
from requests_html import HTMLSession

def myabandonwareSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://www.myabandonware.com/search/q/"+search)

        titles = r.html.find('.name')
        link = r.html.find('.name')

        for i in range (0, len(titles)):
            try:
                results.append(titles[i].text)
                results.append("https://www.myabandonware.com"+link[i].attrs['href'])
            except:
                pass

        if titles == []:
            results.append("Nothing Found")
        
        results = zip(results[::2], results[1::2])
        return(results)
    except:
        results = ["My Abandonware: Connection Failed!"]
        return(results)
