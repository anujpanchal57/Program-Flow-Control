# This is a tuple, so the print command will print the tuple
t = "a", "b", "c"
print(t)

# This is a normal print stmt which will print : a, b, c
print("a", "b", "c")

# This will print the tuple : ('a', 'b', 'c')
print(("a", "b", "c"))

# Tuples declared
welcome = "Welcome to my Page", "Anuj Panchal", 1995
chainsmokers = "Young", "Bloodstream", "Wake up alone", 2016
OneRepublic = "Future looks good", "Kids", 2016
# Tuples within tuples
# Coldplay = "Paradise", "Yellow", 2015, (
#     (1, "Hymn for the weekend"), (2, "Every Teardrop is a waterfall"))

# We can also have same but all the entries in a single tuple
# Coldplay = "Paradise", "Yellow", 2015, (
#     1, "Hymn for the weekend", 2, "Every Teardrop is a waterfall")

# Declaring tuples for printing them individually
Coldplay = "Paradise", "Yellow", 2015, (1, "Hymn for the weekend"), (2, "Every Teardrop is a waterfall")

print(Coldplay)

# We can also print individual tracks
song1, song2, year, track1, track2 = Coldplay
print(song1)
print(song2)
print(year)
print(track1)
print(track2)
Prints the values present in the tuple chainsmokers
print(chainsmokers)

# Prints the respective values present in the tuple
print(chainsmokers[0])
print(chainsmokers[1])
print(chainsmokers[2])
print(chainsmokers[3])

# This stmt will give an error, because we cannot add/append values to the tuples
chainsmokers[0] = "Closer"

chainsmokers2 = ["Honest", "Selfie", 2014]
print(chainsmokers2)

chainsmokers2.append("Don't let me down")

# Prints out Scientist in place of Yellow
Coldplay = Coldplay[0], "Scientist", Coldplay[2]
print(Coldplay)

# Prints the individual values in the tuple as assigned to them
song1, song2, year = chainsmokers2
print(song1)
print(song2)
print(year)

imelda = "More Mayhem", "Imelda May", 2011, ([(1, "Pulling the rug"), (2, "Pyscho"), (3, "Mayhem"),
                                              (4, "Kentish Town Waltz")])

print(imelda)

# Immutable but still we can append
imelda[3].append((5, "All for you"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title, artist, year)

for song in tracks:
    # Additionally, we can also print out track and title separately
    track, title = song
    print("\t Track number: {}, Title: {}".format(track, title))


