import flask
from flask import send_file
from flask import request
from flask import redirect
from waitress import serve

app = flask.Flask(__name__)


@app.route('/download/', methods=['GET'])
def download():
    print("## Headers in download: ", request.headers)
    return redirect("http://127.0.0.1:1245/yay/", code=302)
    # return send_file("./Resources/dye.mp3",as_attachment=True)

@app.route('/yay/', methods=['GET'])
def yay():
    print("## Headers in yay: ", request.headers)
    return send_file("./Resources/dye.mp3",as_attachment=True)

# if __name__ == "__main__":
# app.run()
serve(app, host="127.0.0.1", port=1245)