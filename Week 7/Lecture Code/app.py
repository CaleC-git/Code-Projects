from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import db

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("feedback_form.html")

if __name__ == "__main__":
    app.run(debug=True)