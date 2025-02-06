# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_more_than_5_5(movie):
    return movie['imdb'] > 5.5

def filter_imdb(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

def filter_category(movies, category_name):
    return [movie for movie in movies if movie['category'] == category_name]

def average_imdb(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

print(is_more_than_5_5(movies[0]))  # True

# Movies with IMDB above 5.5
filtered_movies = filter_imdb(movies)
print("IMDB above 5.5:")
for movie in filtered_movies:
    print(f'{movie["name"]}: {movie["imdb"]}')

# "Romance" category
romance_movies = filter_category(movies, "Romance")
print("\nRomance Movies:")
for movie in romance_movies:
    print(f'{movie["name"]}: {movie["imdb"]}')

# Compute the average IMDB of all movies
average_score = average_imdb(movies)
print(f"\nAverage IMDB: {average_score}")
