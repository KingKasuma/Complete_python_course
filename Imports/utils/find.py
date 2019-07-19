#from .common.file_operations import save_to_file
#import utils.common.file_operations

def find_id(iterable, finder, excepted):
    for i in iterable:
        if finder(i) == excepted:
            return i    
    raise NotFoundError(f'{excepted} not found in provided iterable.')

class NotFoundError(Exception):
    pass

if __name__ == '__main__':
    print(find_id(['Rolf', 'Jose', 'Jen'], lambda x: x, 'Jose'))