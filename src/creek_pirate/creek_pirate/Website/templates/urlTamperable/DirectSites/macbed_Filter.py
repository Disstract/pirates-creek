#https://www.macbed.com/?s=
from requests.sessions import session
from requests_html import HTMLSession

def macbedSearch(search):
    results = []

    session = HTMLSession()
    r = session.get("https://www.macbed.com/?s="+search)
    
    titles = r.html.find('.post-title a')
    for i in range(0, len(titles)):
            results.append(titles[i].text)
            results.append(titles[i].attrs['href'])

    if results == []:
        results.append("Nothing Found")
    return(results)




