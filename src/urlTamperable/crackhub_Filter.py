from requests_html import HTMLSession

search = str(input("Enter Search: "))

session = HTMLSession()
r = session.get("https://crackhub.site/?s="+search)

data = r.html.find('.entry-title')

for i in range(0, len(data)):
    print(data[i].text)

