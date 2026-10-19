from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pineapples.html")

@app.route('/favfruit')
def pineapple():
    return render_template("pineapple_two.html")

@app.route('/three/<name>')
def three(name):
    newList = ["haw", "hee", "haha"]
    newDict = {"color":"yellow","taste":"fresh"}
    return render_template("pineapple_three.html",
                            someNewVar = name,
                            someNewList = newList,
                            someNewDict = newDict)

app.run(debug=True)