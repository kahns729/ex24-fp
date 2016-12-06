import os.path



def increment_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	current_count = read_count()
	with open(filename, 'w+') as f:
		f.write(str(current_count + 1))

def decrement_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	current_count = read_count()
	with open(filename, 'w+') as f:
		f.write(str(current_count - 1))

def read_count():
	if os.path.isfile('./count.txt'):
		filename = './count.txt'
	else:
		filename = '/var/www/html/app/count.txt'
	with open(filename, 'r') as f:
		return int(f.read().rstrip())