from flask import Flask
app = Flask(__name__)

@app.route("/")
def work_state():
    return "<h1>App is Running</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
