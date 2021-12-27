from requests_html import HTMLSession
import time

# search = str(input("Enter Search: "))
def crackhubSceneSearch(search):
    results = []
    try:
        session = HTMLSession()
        r = session.get("https://scene.crackhub.site/?s="+search)

        titles = r.html.find('.entry-title a')

        for i in titles:
            print(i)

        for i in range(0, len(titles)):
            results.append(titles[i].text)
            try:
                results.append(titles[i].attrs['href'])
            except:
                pass
            return(results)
    except:
        return("Crackhub Scene: Connection Failed!")

#search = input("enter: ")
#print(crackhubSceneSearch(search))
