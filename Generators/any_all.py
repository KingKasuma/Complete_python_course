friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby) > 0: # True if there's at least one; or False if empty
    print('You are noy alone!')

print(all([0,1,2,3,4,5]))

"""
* 0, 0.0
* None
* [], (), {}
* False
"""