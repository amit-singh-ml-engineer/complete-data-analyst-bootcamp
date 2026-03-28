from flask import Flask
'''
it creates an instance of flask class,
which will be yor WSGI (Web Server Gateway Interface) Application

'''
##WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this best flask course.This course is amazing."
@app.route("/index")
def index():
    return "Welcome to my index page."

if __name__=="__main__":
    app.run(debug=True)