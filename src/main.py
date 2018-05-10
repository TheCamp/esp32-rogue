import math
#import _thread

class Zone():

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getStartPosition(self):
		return {'x': math.floor(self.width / 2), 'y': math.floor(self.height / 2) }

	def tick():
		print("meh")


class Object():

	def __init__(self, x, y, char):
		self.x = x
		self.y = y
		self.char = char

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

class Player(Object):

	def __init__(self, name, *kwargs):
		self.name = name
		super(Player, self).__init__(*kwargs)

def main():
	zone = Zone(10, 10)
	startLocation = zone.getStartPosition()
	player = Player('meh', startLocation['x'], startLocation['y'], '@')
	print(player.x, player.y, player.char)


if __name__ == '__main__':
	main()