#https://gog-games.com/search/enter
from requests_html import HTMLSession
import time

def gogGamesSearch(search):
    try:
        session = HTMLSession()
        r = session.get("https://gog-games.com/search/"+search)

        titles = r.html.find('.title')
        link = r.html.find('.block')

        print("\n-----------!!GOG Games!!-----------")
        if titles == []:
            print("Nothing Found")
            print("------------------------------")
        else:
            for i in range(0, len(titles)):
                
                print(titles[i].text)
                print("https://gog-games.com"+link[i].attrs['href'])

                print("------------------------------")
                time.sleep(0.05)
    except:
        print("\n-----------!!GOG Games!!-----------")
        print("Couldn't connect")
        print("------------------------------")