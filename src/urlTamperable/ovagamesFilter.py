from requests_html import HTMLSession
import time

def ovaGamesSearch(search):
    try:
        session = HTMLSession()
        r = session.get("https://www.ovagames.com/?s="+search)

        titles = r.html.find('.post-title a')

        print("\n-----------!!OVA Games!!-----------")
        if titles == []:
            print("Nothing Found")
            print("------------------------------")
        else:
            for i in range(0, len(titles)):
                
                print(titles[i].text)
                print(titles[i].attrs['href'])

                print("------------------------------")
                time.sleep(0.05)
    except:
        print("\n-----------!!OVA Games!!-----------")
        print("Couldn't connect")
        print("------------------------------")