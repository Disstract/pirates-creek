from requests_html import HTMLSession
import time

def crackhubSearch(search):
    session = HTMLSession()
    r = session.get("https://crackhub.site/?s="+search)

    titles = r.html.find('.entry-title')
    try:
        link = r.html.find('.entry-title a')
    except:
        pass

    print("\n-----------!!Crackhub!!-----------")
    for i in range(0, len(titles)):
        print(titles[i].text)
        try:
            print(link[i].attrs['href'])
        except:
            pass
        print("------------------------------")
        time.sleep(0.05)
    

