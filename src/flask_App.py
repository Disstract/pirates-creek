from flask import Flask, render_template, request
import os
from urlTamperable.DirectSites import crackhub_Filter, crackhubScene_Filter, gloadFilter, gogGamesFilter, ovagamesFilter, scooter_Filter, myabandonwareFilter, macbed_Filter, oldgamesdownloadFilter
from urlTamperable.Repacks import chovkaRepackFilter, fitgirlRepackFilter, gnarlyFilter
import random, threading, webbrowser

# ~ Initialise
app = Flask(__name__, template_folder='template')

# ~ Setup the home/index page
@app.route('/')
def main():
    return render_template("website.html")

@app.route('/result', methods = ["POST","GET"])
def result():
    # ~ convert to dictionary 
    result = request.form.to_dict() 
    
    result = result["search"]

	# ~ actually perform all the searches
    oldgamesdownloadfilter = oldgamesdownloadFilter.oldgamesdownloadSearch(result)
    
    myabandonware = myabandonwareFilter.myabandonwareSearch(result)
    
    crackhub = crackhub_Filter.crackhubSearch(result)

    crackhubscene = crackhubScene_Filter.crackhubSceneSearch(result)
    
    gload = gloadFilter.gloadSearch(result)
    
    gnarly = gnarlyFilter.gnarlySearch(result)

    ova = ovagamesFilter.ovaGamesSearch(result)

    scooter = scooter_Filter.scooterSearch(result)

    gogGames = gogGamesFilter.gogGamesSearch(result)

    chovka = chovkaRepackFilter.chovkaSearch(result)

    macbed = macbed_Filter.macbedSearch(result)

	# ~ add shortcut
    romlink = "#rom"

    romtext = "Jump to ROMS/Retro games"
            
    # ~ render using website.html        
    return render_template("website.html", result = result, romlink = romlink, romtext = romtext, ova=ova, oldgamesdownloadfilter = oldgamesdownloadfilter, myabandonware = myabandonware, crackhub = crackhub, crackhubscene=crackhubscene, gload = gload, scooter = scooter, gnarly = gnarly, gogGames = gogGames, chovka = chovka, macbed = macbed)


if __name__ == "__main__":

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(port=port, debug=False)




'''
Some useful tips for you:
 - if you're having issues running the app, try:
 - export FLASK_APP=flask_App.py
 - flask run
 - or just run through idle if it doesn't work

this might be useful(for css and js folder structure): https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html 
'''
    
