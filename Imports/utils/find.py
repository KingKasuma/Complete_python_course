from .common.file_operations import save_to_file

def find_id(iterable, finder, excepted):
    for i in iterable:
        if finder(i) == excepted:
            return i    
    raise NotFoundError(f'{excepted} not found in provided iterable.')

class NotFoundError(Exception):
    pass

print(__name__)