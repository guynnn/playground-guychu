import flask
from flask import send_file
from flask import request
from flask import redirect

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/download', methods=['GET'])
def home():
    print("## Headers in download: ", request.headers)
    return redirect("127.0.0.1:5000/yay", code=302)
    # return send_file("./Resources/dye.mp3",as_attachment=True)

@app.route('/yay', methods=['GET'])
def yay():
    print("## Headers in yay: ", request.headers)
    return send_file("./Resources/dye.mp3",as_attachment=True)

app.run()
