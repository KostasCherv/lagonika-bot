import datetime

def log(msg):
	timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print(f"{timestamp}: {msg}")