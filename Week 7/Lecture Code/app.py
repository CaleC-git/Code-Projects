from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import db

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "user_feedback_images"

@app.route("/")
def homepage(): # Opens app to a homepage
    return render_template("feedback_form.html")

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback(): # This'll read data and images from the form as well as save to the DB
    # reading the data from form
    feedback = request.form.to_dict()
    print(feedback)

    # reading and saving the image
    image_file = request.files["image"]
    if image_file.filename:
        save_filename = f'{uuid.uuid4()}_{image_file.filename}'
        save_location = os.path.join(app.config["UPLOAD_FOLDER"], save_filename)
        print(save_filename)
        print(save_location)
        image_file.save(save_location)
        feedback["image_path"] = save_filename

    # saving the data to DB
    db.save_feedback(feedback)


    return render_template("thank_you.html")


@app.route("/admin")
def admin_page():
    feedbacks = db.get_all_feedback()
    if feedbacks is None:
        feedbacks = []

    feedback_count = len(feedbacks)
    user_image_location = app.config["UPLOAD_FOLDER"]

    return render_template("admin.html", feedback_count=feedback_count, feedbacks=feedbacks, user_image_location=user_image_location)


@app.route("/user_feedback_images/<filename>")
def user_feedback_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)