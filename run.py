import os #import os from Python
from flask import Flask, render_template #import Flask class, and render_template function from flask framework

app = Flask(__name__) #store instance of Flask in variable named "app"


@app.route("/") #defines the route that triggers the index function, the "/" indicates the root directory
def index():
    return render_template("index.html") #Flasks expects templates inside "templates" directory


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__": #Main is default module in Python, run directly if not imported
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), #use os module to get IP variable environment variable if it exists, or set default if not found
        port=int(os.environ.get("PORT", "5000")), #set default port for Flask (5000 is a common port)
        debug=True) #Allow debugging of code during dev stage