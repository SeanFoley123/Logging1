import logging
import module_using_logging
#Testing out the name keyword.
logging.basicConfig(filename = 'output.txt', filemode = 'w', format = '%(name)s:%(message)s')
logging.warning('This is a file')
logging.info('I knew that!')
module_using_logging.whats_my_name()