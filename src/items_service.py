import json
from src.item import Item

from src.my_logger import log

class ItemsService:
	def __init__(self, filename):
		self.filename = filename
		self._create_file()

	def _create_file(self):
		try:
			with open(self.filename, 'r') as f:
				pass
		except FileNotFoundError:
			self.update([])

	def get(self)-> list[Item]:
		existingItems = []
		try:
			with open(self.filename, 'r') as f:
				existingItems = json.load(f)
		except FileNotFoundError as e:
			log(e)
		
		return existingItems

	def update(self, items: list[Item]):
		try:
			with open(self.filename, 'w') as f:
				json.dump(items, f, default=lambda o: o.__dict__)
		except Exception as e:
			log(e)
			self.update([])
