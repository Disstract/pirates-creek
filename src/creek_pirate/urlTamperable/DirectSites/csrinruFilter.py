from requests_html import HTMLSession
import time


search = str(input("Enter Search: "))
# def csrinruSearch(search):
session = HTMLSession()
r = session.get("https://cs.rin.ru/forum/search.php?keywords="+search+"&terms=any&author=&sc=1&sf=titleonly&sk=t&sd=d&sr=topics&st=0&ch=300&t=0&submit=Search")

titles = r.html.find('.topictitle')

print(titles)
