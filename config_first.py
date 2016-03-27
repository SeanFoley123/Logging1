import logging
# You gotta put basicConfig before you log anything!
# logging.warning('hi')
logging.basicConfig(filename = 'output.txt')
logging.warning('This is a file')
logging.info('I knew that!')