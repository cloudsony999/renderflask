from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<body bgcolor='green' text='yellow'><center><h2>I am Flask from Cloud!!!</h2></body>"


if __name__=='__main__':
    app.run()

    
