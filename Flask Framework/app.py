from flask import Flask
'''
It creates an instance of the Flask class,
#which will be your WSGI app
'''

#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course. This is an amazing course"

@app.route("/index")
def index():
    return "This is the index page"

if __name__=="__main__":
    app.run(debug=True)