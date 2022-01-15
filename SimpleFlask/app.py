from flask import Flask, render_template, Response
import random

app = Flask(__name__)

@app.route("/myStatus")
def getStatus():
    state = random.randint(1,5)
    if state % 2 == 0:
        status = " On"
    else:
        status = "Off"
    print(status)
    return status


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')