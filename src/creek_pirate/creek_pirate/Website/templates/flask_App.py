from flask import Flask, render_template, request
import jinja2

from urlTamperable.DirectSites import crackhub_Filter, crackhubScene_Filter, gloadFilter, gogGamesFilter, ovagamesFilter
from urlTamperable.Repacks import chovkaRepackFilter, fitgirlRepackFilter

env = jinja2.Environment()
env.globals.update(zip=zip)

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
    result = chovkaRepackFilter.chovkaSearch(result)
    result = zip(result[::2], result[1::2]) 


    return render_template("website.html", result = result) 

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

    '''
    export FLASK_APP=flask_App.py
    flask run
    or just run thur idle if it doesn't work
    https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html = for css and js folder structure
    https://codepen.io/huange/pen/rbqsD where i got the search bar code from
    '''
    
