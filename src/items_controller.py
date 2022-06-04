import json

class ItemsController:
	def __init__(self, filename):
		self.filename = filename
		self._create_file()

	def _create_file(self):
		try:
			with open(self.filename, 'r') as f:
				pass
		except FileNotFoundError:
			self.update([])

	def get(self):
		existingItems = []
		try:
			with open(self.filename, 'r') as f:
				existingItems = json.load(f)
		except FileNotFoundError:
			pass
		
		return existingItems

	def update(self, items):
		with open(self.filename, 'w') as f:
			json.dump(items, f)