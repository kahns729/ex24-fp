def increment_count():
	current_count = get_count()
	with open('./count.txt', 'w+') as f:
		f.write(str(current_count + 1))

def decrement_count():
	current_count = get_count()
	with open('./count.txt', 'w+') as f:
		f.write(str(current_count - 1))

def get_count():
	with open('./count.txt', 'r') as f:
		return int(f.read().rstrip())