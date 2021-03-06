class Stack(object):
	def __init__(self):
		self._data = []

	def push(self, item):
		self._data.append(item)

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data.pop()

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data[-1]

	def is_empty(self):
		return len(self._data) == 0

	def __len__(self):
		return len(self._data)


class Empty(Exception):
	pass