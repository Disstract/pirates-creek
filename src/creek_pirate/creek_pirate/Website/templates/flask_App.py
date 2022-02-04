from flask import Flask, render_template, request

from urlTamperable.DirectSites import crackhub_Filter, crackhubScene_Filter, gloadFilter, gogGamesFilter, ovagamesFilter, scooter_Filter, myabandonwareFilter, oldgamesdownloadFilter
from urlTamperable.Repacks import chovkaRepackFilter, fitgirlRepackFilter, gnarlyFilter

app = Flask(__name__, template_folder='template')


# array = ["eeee", "bbbb", "aaaa", "cccc"]
# array = zip(array[::2], array[1::2])

@app.route('/')
def main():
    return render_template("website.html")

@app.route('/result', methods = ["POST","GET"])
def result():
    result = request.form.to_dict()
    result = result["search"]

    oldgamesdownload = oldgamesdownloadFilter.oldgamesSearch(result)
    oldgamesdownload = zip(oldgamesdownload[::2], oldgamesdownload[1::2])
    
    myabandonware = myabandonwareFilter.myabandonwareSearch(result)
    myabandonware = zip(myabandonware[::2], myabandonware[1::2])
    
    crackhub = crackhub_Filter.crackhubSearch(result)
    crackhub = zip(crackhub[::2], crackhub[1::2]) 

    crackhubscene = crackhubScene_Filter.crackhubSceneSearch(result)
    crackhubscene = zip(crackhubscene[::2], crackhubscene[1::2])
    
    gload = gloadFilter.gloadSearch(result)
    gload = zip(gload[::2], gload[1::2])
    
    gnarly = gnarlyFilter.gnarlySearch(result)
    gnarly = zip(gnarly[::2], gnarly[1::2])

    ova = ovagamesFilter.ovaGamesSearch(result)
    ova = zip(ova[::2], ova[1::2])

    scooter = scooter_Filter.scooterSearch(result)
    scooter = zip(scooter[::2], scooter[1::2])

    gogGames = gogGamesFilter.gogGamesSearch(result)
    gogGames = zip(gogGames[::2], gogGames[1::2])


    chovka = chovkaRepackFilter.chovkaSearch(result)
    chovka = zip(chovka[::2], chovka[1::2]) 

   
        
    return render_template("website.html", result = result, ova=ova, oldgamesdownload = oldgamesdownload, myabandonware = myabandonware, crackhub = crackhub, crackhubscene=crackhubscene, gload = gload, scooter = scooter, gnarly = gnarly, gogGames = gogGames, chovka = chovka)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3912, debug=True)




'''
export FLASK_APP=flask_App.py
flask run
or just run thur idle if it doesn't work
https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html = for css and js folder structure


https://www.knowledgewalls.com/johnpeter/books/good-javascript-examples/how-to-create-multiselect-combobox-with-checkbox-in-javascript-and-html-with-example
'''
    
