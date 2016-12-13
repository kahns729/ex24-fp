import os.path
import sqlite3, time

def update_db(timestamp, count):
	if os.path.isfile('./counts.db'):
		filename = './counts.db'
	else:
		filename = '/var/www/html/app/counts.db'
	conn = sqlite3.connect(filename)
	c = conn.cursor()
	c.execute('INSERT INTO counts VALUES (?, ?);', (timestamp, count))
	conn.commit()
	conn.close()

def increment_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	current_count = read_count()
	with open(filename, 'w+') as f:
		f.write(str(current_count + 1))
	update_db(int(time.time()), current_count + 1)

def decrement_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	current_count = read_count()
	with open(filename, 'w+') as f:
		f.write(str(current_count - 1))
	update_db(int(time.time()), current_count - 1)

def read_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	with open(filename, 'r') as f:
		return int(f.read().rstrip())