from flask import Flask


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "starting ml project from ci cd completed"


if __name__=="__main__":
    app.run(debug=True)    