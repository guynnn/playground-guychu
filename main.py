import flask
from flask import send_file
from flask import request
# from flask import redirect
import os

app = flask.Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    print("## Headers in download: ", request.headers)
    song_name = request.args.get('song_name')
    print("##", song_name)
    return send_file("./Resources/" + song_name + ".mp3", as_attachment=True)


# def redirect():
#     print("## Headers in download: ", request.headers)
#     return redirect("yay", code=302)


if __name__ == "__main__":
    port = os.environ.get("port", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)