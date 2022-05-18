current_movies = {
    'The Grinch': '11am',
    'Rudolph': '1pm',
    'Frosty the Snowman': '3pm',
    'Christmas Vacation': '5pm'
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, ' is playing at ', showtime, sep='')
