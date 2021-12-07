from requests_html import HTMLSession
import time

search = str(input("Enter Search: "))

session = HTMLSession()
r = session.get("https://scene.crackhub.site/?s="+search)

titles = r.html.find('.entry-title')
try:
    link = r.html.find('.entry-title a')
except:
    pass

print("\n-----------!!Crackhub Scene!!-----------")
for i in range(0, len(titles)):
    print(titles[i].text)
    try:
        print(link[i].attrs['href'])
    except:
        pass
    print("------------------------------")
    time.sleep(0.05)
    

