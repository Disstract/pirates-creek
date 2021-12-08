from requests_html import HTMLSession
import time

def chovkaSearch(search):
    try:
        session = HTMLSession()
        r = session.get("https://repack.info/search/"+search)

        titles = r.html.find('.title')
        link = r.html.find('.text-dark')

        print("\n-----------!!Chovka Repacks!!-----------")
        for i in range(0, len(titles)):
            print(titles[i].text)
            try:
                print(link[i].attrs['href'])
            except:
                pass
            print("------------------------------")
            time.sleep(0.05)
    except:
        print("\n-----------!!Chovka Repacks!!-----------")
        print("Couldn't connect")
        print("------------------------------")