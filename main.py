from flask import Flask, render_template, request
from Jumble import jumble

words_list = jumble.getword_list()
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()