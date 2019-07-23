friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends)
friends_lower = [friend.lower() for friend in friends] # List Comprehension
friends_lower = (friend.lower() for friend in friends) # Generator Comprehension

print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

users = [User.from_dict(user) for user in users] # List Comprehension
users = map(User.from_dict, users)