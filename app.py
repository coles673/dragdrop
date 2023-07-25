from flask import Flask, render_template, request, redirect, url_for
from flask_dropzone import Dropzone
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
import yaml

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["DROPZONE_ALLOWED_FILE_CUSTOM"] = True
app.config["DROPZONE_ALLOWED_FILE_TYPE"] = ".yaml"
app.config["DROPZONE_MAX_FILE_SIZE"] = 3  # Max file size in MB
app.config["DROPZONE_MAX_FILES"] = 1

dropzone = Dropzone(app)


class UploadForm(FlaskForm):
    yaml_file = FileField("Upload YAML File")
    submit = SubmitField("Upload")


UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def validate_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            yaml_data = yaml.safe_load(file)
            # Add your custom validation logic here if needed
            return True
    except yaml.YAMLError as e:
        print("Error parsing YAML:", e)
        return False


@app.route("/", methods=["GET", "POST"])
def upload_file():
    form = UploadForm()
    if request.method == "POST" and form.validate_on_submit():
        yaml_file = form.yaml_file.data

        # Check if the file has a valid extension and save it
        # if yaml_file and yaml_file.filename.endswith(".yaml"):
        #     # filename = secure_filename(yaml_file.filename)
        #     file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        #     yaml_file.save(file_path)

        # Perform YAML file validation
        # if validate_yaml(file_path):
        #         return "File uploaded and validated successfully!"
        #     else:
        #         # os.remove(file_path)
        #         return "Invalid YAML file. Please check the file and try again."

        # else:
        #     return "Invalid file format. Only YAML files are allowed."

    return render_template("upload.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
