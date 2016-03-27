import logging
# Logging can handle a lot of things. It fills in the value of a when I tell it to log that, so the log says 1 instead 
# of just converting the letter a to a string. Cool!
class Mushroom(object):
	def __init__(self, frogs):
		self.frogs = frogs
def main():
	logging.basicConfig(filename = 'output.txt', filemode = 'w')
	logging.warning('This is a file')
	logging.info('I knew that!')
	a = 1
	bill = Mushroom(2)
	logging.critical(a)
	logging.warning([1, 2, 3])
	logging.error({'a': 1, 'b': 3})
	logging.critical(bill)
main()