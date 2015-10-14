from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def i1();
    return "Hello World"

@app.route("/user/paul/")
def i2();
    return "User Paul"

@app.route("/post/80")
def i3
    return "Post 80"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080,debug=True)
