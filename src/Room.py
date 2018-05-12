class Room
	def __init__(self, id, height = 10, width = 10):
		self.id = id
		self.height = height
		self.width = width
		self.room_map = [[0 for x in range(width)] for y in range(height)]
		self.room_size = height * width