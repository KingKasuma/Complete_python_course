"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[X]: Decide where to store movies
[X]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[X]: Allow users to add movies
[X]: Show all their movies
[]: Find a movie
[X]: Stop running the program when they type 'q'
"""

movies = []

"""
movies = {
    'name': ...(str),
    'director': ...(str),
    'year': ... (int)
}
"""

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command-please try again.')

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

def add_movie():
    name = input('Enter the movie: ')
    director = input('Enter the director: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attributes(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attributes(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
