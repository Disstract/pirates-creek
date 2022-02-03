from requests_html import HTMLSession
import time

def gnarlySearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://www.gnarly-repacks.site/?s="+search)

        link = r.html.find('.loop-entry-title a')
        time.sleep(0.05)

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
        results = ["Gnarly Repacks: Connection Failed!"]
        return(results)

