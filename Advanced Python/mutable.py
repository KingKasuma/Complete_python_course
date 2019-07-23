friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0 # friends_last_seen.__setitem__(self,'Rolf')
print(id(friends_last_seen))

#That are inmutable
my_int = 5
print(id(my_int))

my_int = my_int + 1 # my_int.__add__(self, 1): return self.value += 1
my_int += 1 # my_int.__iadd__(self, 1)
print(id(my_int))

# Lists are mutable
friends = ['Rolf', 'Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

""" Inmutables Types
integers -> all functions return new int objects
floats
strings
tuples
"""
print("####################################################################################")
##########################################################################################
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

######### anohter example #######
primes = [2,3,5]

print(id(primes))

primes += [7,11] # primes = primes.__iadd__([7, 11])
print(id(primes))

