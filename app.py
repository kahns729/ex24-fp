from flask import Flask, render_template, jsonify
from count import increment_count, decrement_count, get_count
import os
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
	   # Advanced usage:
	# editing the 'dirnames' list will stop os.walk() from recursing into there.

	for dirname, dirnames, filenames in os.walk('.'):
		if '.git' in dirnames:
			# don't go into any .git directories.
			dirnames.remove('.git')
		# print path to all subdirectories first.
		for subdirname in dirnames:
			print(os.path.join(dirname, subdirname))

		# print path to all filenames.
		for filename in filenames:
			print(os.path.join(dirname, filename))


	current_count = get_count()
	return render_template('index.html', num=current_count)

@app.route('/increment', methods=['POST'])
def increment():
	increment_count()
	return jsonify(result={"status": 200})

@app.route('/decrement', methods=['POST'])
def decrement():
	decrement_count()
	return jsonify(result={"status": 200})


if __name__ == '__main__':
  app.run()
