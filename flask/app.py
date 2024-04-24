from flask import Flask
# import app

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome Home</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)