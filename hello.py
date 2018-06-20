from flask import Frlask,render_template,url_for
myapp=Flask(__name__)
@myapp.route("/")
def hello():
    return render_template("index.html")
