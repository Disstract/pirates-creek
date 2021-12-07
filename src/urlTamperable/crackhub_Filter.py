from requests_html import HTMLSession
import time

search = str(input("Enter Search: "))

session = HTMLSession()
r = session.get("https://crackhub.site/?s="+search)

titles = r.html.find('.entry-title')
link = r.html.find('.entry-title a')

print("\n-----------!!Crackhub!!-----------")
for i in range(0, len(titles)):
    print(titles[i].text)
    print(link[i].attrs['href'])
    print("------------------------------")
    time.sleep(0.05)
    

