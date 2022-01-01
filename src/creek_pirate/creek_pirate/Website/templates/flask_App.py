from flask import Flask, render_template, request

from urlTamperable.DirectSites import crackhub_Filter, crackhubScene_Filter, gloadFilter, gogGamesFilter, ovagamesFilter
from urlTamperable.Repacks import chovkaRepackFilter, fitgirlRepackFilter

app = Flask(__name__, template_folder='template')


array = ["eeee", "bbbb", "aaaa", "cccc"]
array = zip(array[::2], array[1::2])

@app.route('/')
def main():
    return render_template("website.html")

@app.route('/result', methods = ["POST","GET"])
def result():
    result = request.form.to_dict()
    result = result["search"]
    
    crackhub = crackhub_Filter.crackhubSearch(result)
    crackhub = zip(crackhub[::2], crackhub[1::2]) 

    gload = gloadFilter.gloadSearch(result)
    gload = zip(gload[::2], gload[1::2])

    gogGames = gogGamesFilter.gogGamesSearch(result)
    gogGames = zip(gogGames[::2], gogGames[1::2])


    chovka = chovkaRepackFilter.chovkaSearch(result)
    chovka = zip(chovka[::2], chovka[1::2]) 


    return render_template("website.html", crackhub = crackhub, gload = gload, gogGames = gogGames, chovka = chovka)

@app.route('/settings', methods = ["POST","GET"])
def settings():
    return render_template("settings.html")



if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)




'''
export FLASK_APP=flask_App.py
flask run
or just run thur idle if it doesn't work
https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html = for css and js folder structure


https://www.knowledgewalls.com/johnpeter/books/good-javascript-examples/how-to-create-multiselect-combobox-with-checkbox-in-javascript-and-html-with-example
'''
    
