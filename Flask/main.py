from flask import Flask
app = Flask(__name__)

# decorator function = @, can loosely think of it as an event callback

@app.route("/")
def index():
        return ' Hello CART 351! '


@app.route("/about")
def about():
        return '<h1 style = "color:purple"> About Cart 351!</h1>'

@app.route("/user/<name>")
def userProfile(name):
        return f'U ARE {name}'

@app.route("/cat/<catname>")
def catNamer(catname):
    if catname.endswith("y"):
           test = catname.rpartition("y")
           catname = test
           return catname

app.run()