from flask import Flask 
app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome, Fellow Pirate. Let us sail the high seas of the internet. '

if __name__ == "__main__":
    app.run(debug=True)