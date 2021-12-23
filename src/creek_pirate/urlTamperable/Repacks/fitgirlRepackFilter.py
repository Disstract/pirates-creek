from requests_html import HTMLSession
import time

def fitgirlSearch(search):
	results = []
	try:
		session = HTMLSession()
		r = session.get("https://fitgirl-repacks.site/?s="+search)

		titles = r.html.find('.entry-title', first=True)
		print(titles.text)
	except:
		return("Fitgirl Repacks: Connection Failed!")
		
