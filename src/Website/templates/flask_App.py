from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route('/')
def main():
    return render_template("website.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)


    '''
    $ export FLASK_APP=flask_App.py
    $ flask run
    or just run thur idle if it doesn't work
    https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html = for css and js folder structure
    '''
    