# LISTS
# A collection of data that is ORDERED & CHANGEABLE []

rockstar_games = ["GTA V", "BULLY", "RED DEAD", "GTA SAN AN"]

# We always reference the position of an item staring at 0
print(rockstar_games[1])

# list within list

ea_games = ["Fifa", "Apex Legends", "Madden"]
rockstar_games = ["GTA V", "BULLY", "RED DEAD", "GTA SAN AN"]

games = [rockstar_games, ea_games]

print(games[0:2])

# Edit a list with the following funtions

rockstar_games.append("Red Dead 2") # Adds an item
rockstar_games.remove("BULLY") # Removes an item
rockstar_games.reverse() # Reverses the lsit
rockstar_games.count("GTA") # Counts the number of time an item is in the list

#---------------------------------------------

# TUPLES

# A collection of data which is ORDERED & UN-CHANGEABLE

# Pretty much the same as lists but the data is read only and we use () not []



#---------------------------------------------

# DICTIONARIES

# A collection of data which is UN- ORDERED & CHANGEABLE,WITH INDEXES

# Again dictionaries are similar they use {:} and a KEY VALUE PAIR

# Key is on the left and value is on the right

film_ratings = {"Inception" : "8/10", "Up" : "10/10", "Shrek" :  "7/10"}

print(film_ratings["Up"])


















