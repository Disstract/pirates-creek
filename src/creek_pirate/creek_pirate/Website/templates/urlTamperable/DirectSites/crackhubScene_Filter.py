from requests_html import HTMLSession
import time

# search = str(input("Enter Search: "))
def crackhubSceneSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://scene.crackhub.site/?s="+search)

        titles = r.html.find('.entry-title a')
        time.sleep(0.05)

    

        for i in range(0, len(titles)):
            results.append(titles[i].text)
            time.sleep(0.05)

            try:
                results.append(link[i].attrs['href'])
            except:
                pass
        if results == []:
            results.append("Nothing Found")
        return(results)
    except:
        results = ["Crackhub Scene: Connection Failed!"]
        return(results)
