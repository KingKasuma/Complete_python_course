friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends) # arg 1: function that returns True/False

another_starts_with_r = (f for f in friends if f.startswith('R'))

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
start_with_r = my_custom_filter(lambda friend: friend.startswith('R'), friends)
# Filter return a generator