from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/miss_you", methods=["POST"])
def miss_you():
    name = request.form["name"]
    return render_template("miss_you.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)