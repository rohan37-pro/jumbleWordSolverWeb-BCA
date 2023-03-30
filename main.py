from flask import Flask, render_template, request, redirect
from Jumble import jumble

words_list = jumble.getword_list()
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():
    if request.method=="POST":
        jumble_word = request.get_data().decode()
        solved_data = jumble.solve(jumble_word, words_list)
        return solved_data

if __name__ == "__main__":
    app.run(debug=True)