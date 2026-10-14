from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "hello!"

@app.route("/about")
def about():
    return "A first flask web app"

if __name__ == "__main__":
    app.run(debug=True)