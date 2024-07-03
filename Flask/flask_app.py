from flask import Flask

flask_app=Flask(__name__)
@flask_app.route("/")
def welcome():
    return "welcome in the data science web application"

@flask_app.route("/index")
def Index():
    return "welcome to the Index Page"

if __name__=="__main__":
    flask_app.run(debug=True)