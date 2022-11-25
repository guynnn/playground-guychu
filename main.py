import flask
from flask import send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return send_file("./Resources/dye.mp3",as_attachment=True)

app.run()
