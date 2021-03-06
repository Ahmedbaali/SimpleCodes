from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/progress')
def progress():
	def generate():
		x = 0
		
		while x <= 100:
			yield "data:" + str(x) + "\n\n"
			x = x + 10
			time.sleep(0.5)

	return Response(generate(), mimetype= 'text/event-stream')

if __name__ == "__main__":
	app.run()





"""import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        i = 0
        while True:
            #json_data = json.dumps(
             #   {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield i #f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)"""