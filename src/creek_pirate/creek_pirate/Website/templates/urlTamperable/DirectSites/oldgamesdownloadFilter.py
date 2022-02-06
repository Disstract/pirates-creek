from requests_html import HTMLSession
def oldgamesSearch(search):
    
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://oldgamesdownload.com/?s="+search)

        titles = r.html.find('.title a')
        
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
        results = ["Old Games Download: Connection Failed!"]
        return(results)

