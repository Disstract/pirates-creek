from requests_html import HTMLSession
import time

def fitgirlSearch(search):
	results = []
	try:
		session = HTMLSession()
		r = session.get("https://fitgirl-repacks.site/?s="+search)

		titles = r.html.find('.entry-title')
		try:
			link = r.html.find('.entry-title a')
		except:
			pass
		
		for i in range(0, len(titles)):
			results.append(titles[i].text)
			try:
				results.append(link[i].attrs['href'])
			except:
				pass
		if results == []:
			results.append("Nothing Found")
		return(results)
	except:
		return("Fitgirl Repacks: Connection Failed!")
		
