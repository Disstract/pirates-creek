from requests.sessions import session
from requests_html import HTMLSession

def scooterSearch(search):
    results = []
    
    try:
        session = HTMLSession()
        r = session.get("https://scooter-repacks.site/?s="+search)

        titles = r.html.find('.entry-title a')
        
        if titles == []:
            results.append("Nothing Found")
        else:
            for i in range(0, len(titles)):
                
                results.append(titles[i].text)
                results.append(titles[i].attrs['href'])
                
        return(results)
        
       
    except:
        return("Scooter: Connection Failed!")
