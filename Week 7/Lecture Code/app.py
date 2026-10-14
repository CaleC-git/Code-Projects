from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import db

app = Flask(__name__)

@app.route("/")
def homepage(): # Opens app to a homepage
    return render_template("feedback_form.html")

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback(): # This'll read data and images from the form as well as save to the DB
    # reading the data from form
    feedback = request.form.to_dict()
    print(feedback)

    # saving the data to DB
    db.save_feedback(feedback)


    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)