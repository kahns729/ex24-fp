from flask import Flask, render_template, jsonify
from count import increment_count, decrement_count, read_count
import os
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
	current_count = read_count()
	return render_template('index.html', num=current_count)

@app.route('/increment', methods=['POST'])
def increment():
	increment_count()
	return jsonify(result={"count": read_count()})

@app.route('/decrement', methods=['POST'])
def decrement():
	decrement_count()
	return jsonify(result={"count": read_count()})

@app.route('/get_count')
def get_count():
	return jsonify(result={"count": read_count()})

if __name__ == '__main__':
  app.run()
