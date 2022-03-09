from flask import render_template
from flask import Flask, request
from tictactoe import result

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("tictactoe_board.html")
    elif request.method == "POST":
        # TODO: proper validation
        return render_template(
            "tictactoe_board.html", result=result(request.form), board=request.form
        )
