import flask
from flask import send_file
from flask import request
from flask import redirect
import os

app = flask.Flask(__name__)

hostName = "playground-guychu.herokuapp.com/"

@app.route('/download/', methods=['GET'])
def download():
    print("## Headers in download: ", request.headers)
    return redirect("https://" + hostName + "yay/", code=302)

@app.route('/yay/', methods=['GET'])
def yay():
    print("## Headers in yay: ", request.headers)
    return send_file("./Resources/dye.mp3", as_attachment=True)


if __name__ == "__main__":
    port = os.environ.get("port", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)