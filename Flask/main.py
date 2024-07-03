from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def hello():
    return "<html><H1>hello in the life of aftab</H1></html>"

@app.route("/index")
def Index():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)

