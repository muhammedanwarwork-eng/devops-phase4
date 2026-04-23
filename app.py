from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Project Successfully Deployed! </h1><p>Running inside Docker via GitHub Actions.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)