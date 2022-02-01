from requests.sessions import session
from requests_html import HTMLSession

def scooterSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://scooter-repacks.site/?s="+search)

        link = r.html.find('.entry-title a')
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
        return("scooter: Connection Failed!")

