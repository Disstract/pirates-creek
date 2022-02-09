from requests.sessions import session
from requests_html import HTMLSession

def scooterSearch(search):
    results = []
    
    try:
        session = HTMLSession()
        r = session.get("https://scooter-repacks.site/?s="+search)

        titles = r.html.find('.entry-title a')

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
        return("Scooter: Connection Failed!")
