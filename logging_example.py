import logging
import os, sys
def print_bears(number):
	print 'bears'*number
	global were_bears
	were_bears = True
	logging.info('He asked for {} bears.'.format(number))

def print_pigs(number):
	print 'pig'*number
	logging.info('He asked for {} pigs.'.format(number))
	if were_bears:
		logging.error('The user does not seem to realize that bears and pigs do not play nicely.')

def print_lemurs(number):
	print 'lemur'*number*10
	logging.info('He asked for {} lemurs.'.format(number))


def main():
	logging.basicConfig(filename = 'log.txt', format = '%(asctime)s %(levelname)s: %(message)s', level = logging.INFO, filemode = 'w')
	global were_bears
	were_bears = False
	functions = {'bear': lambda number: print_bears(number), 'pig': lambda number: print_pigs(number), 'lemur': lambda number: print_lemurs(number)}
	greetings = ['What kind of animal do you want? ', 'What kind of animal do you want now? ']
	time = 0
	os.system('clear')
	while True:
		kind = raw_input(greetings[time]).lower()
		if kind == 'help':
			print "We've got bears, pigs, and lemurs."
			time = 1
			continue
		elif kind == 'exit':
			sys.exit()
		elif kind not in functions:
			raw_input("We don't have that animal here, kid. Press enter to pick a better animal.")
			logging.critical('The user is asking for non-existent animmals. If this continues, our cover may be blown.')
			continue
		try:
			number = input('How many? ')
			if not isinstance(number, int):	
				raise Exception
		except:
			while not isinstance(number, int):	
				number = input("Didn't catch that. How many? ")
				print type(number)
				logging.info('User does not seem to have a firm grasp of numbers.')
		functions[kind](number)
		time = 1




if __name__ == '__main__':
	main()