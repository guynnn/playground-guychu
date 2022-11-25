import flask
from flask import send_file
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    print("## Headers: ", request.headers)
    return send_file("./Resources/dye.mp3",as_attachment=True)

app.run()
