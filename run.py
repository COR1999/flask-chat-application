import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}

    messages.append(messages_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main message with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """Display chat messsages"""
    return render_template("chat.html", username=username, chat_messages=messages)


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=True)
