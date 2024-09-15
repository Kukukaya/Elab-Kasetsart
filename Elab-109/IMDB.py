#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
#data = read_json(filename)
### ----------------------------------------------------------
#------------------------------------------- IMDB HEADER -------------------------------------------

data = read_json(filename)

data = read_json(filename)

def q1():
    movie_filtered = [
        x for x in data 
        if x.get("cast") 
        and "Harrison Ford" in [y["name"] for y in x["cast"]] 
        and x["director"]["name"] != "Steven Spielberg" 
        and x.get("ratingValue")
    ]
    
    movie_filtered.sort(key=lambda x: float(x["ratingValue"]), reverse=True)
    top_five = []
    top_ratings = set()
    
    for movie in movie_filtered:
        if len(top_ratings) < 5 or float(movie["ratingValue"]) in top_ratings:
            top_ratings.add(float(movie["ratingValue"]))
            top_five.append(movie["director"]["name"])
        elif len(top_ratings) == 5:
            break
            
    for director in sorted(set(top_five)):
        print(director)


def q2():
    movie_harrison = []
    movie_no_director = []
    top_film = []

    movie_harrison = [m for m in data if m.get("cast") if "Harrison Ford" in [y["name"] for y in m["cast"]] and "Tommy Lee Jones" in [y["name"] for y in m["cast"]]]
    movie_no_director = [x for x in movie_harrison if x["director"]["name"] != "Steven Spielberg" and x["director"]["name"] != "George Lucas" and x["ratingValue"]]
    movie_no_director.sort(key=lambda x: float(x["ratingValue"]), reverse=True)

    top_film = movie_no_director[0]
    print(top_film['name'])

def q2():
    movie_harrison = []
    movie_no_director = []
    top_film = []

    movie_harrison = [m for m in data if m.get("cast") if "Harrison Ford" in [y["name"] for y in m["cast"]] and "Tommy Lee Jones" in [y["name"] for y in m["cast"]]]
    movie_no_director = [x for x in movie_harrison if x["director"]["name"] != "Steven Spielberg" and x["director"]["name"] != "George Lucas" and x["ratingValue"]]
    movie_no_director.sort(key=lambda x: float(x["ratingValue"]), reverse=True)

    top_film = movie_no_director[0]
    print(top_film['name'])

# END of line
print("(1) Answer of Q1")
print("(2) Answer of Q2")
ans = input("or just press (Enter): ")

if ans == "1":
    q1()
elif ans == "2":
    q2()
else:
    print("Nothing to do..")