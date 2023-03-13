from flask import Flask


app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return 'Hi, I am on the app'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)


# pip3 install -U Flask