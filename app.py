from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# TODO Add two numbers, 'first' and 'second' as query parameters
# Ex: /add?first=4&second=8 => Returns "12"

# TODO SOLIDWORKS-, 'x' and 'y' as query parameters, repeat "SOLID" x times and "WORKS" y times
# Ex: /repeat?x=1&y=1 => Returns "SOLIDWORKS"

# TODO Look up a book by ID
# Ex: /book/2 => Returns full json object for "100 Years..."

# TODO Return a summary of book stats
# (total books, oldest release year, how many checked out?)