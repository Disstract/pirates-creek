from requests_html import HTMLSession
import time

def gloadSearch(search):
    try:
        session = HTMLSession()
        r = session.get("https://gload.to/?s="+search)

        link = r.html.find('.postsborder a')

        print("\n-----------!!Gload!!-----------")
        if link == []:
            print("Nothing Found")
            print("------------------------------")
        else:
            for i in range(0, len(link)):
                try:
                    print(link[i].attrs['href'])
                except:
                    pass
                print("------------------------------")
                time.sleep(0.05)
    except:
        print("\n-----------!!Gload!!-----------")
        print("Couldn't connect")
        print("------------------------------")