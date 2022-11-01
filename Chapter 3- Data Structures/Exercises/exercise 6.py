guests=["kareem","siraj","amaan"]
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

print("\n Sorry, we can only invite two people to dinner, because of the new table won't arrive on time.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")


name = guests[0].title()
print(name + ",please come to dinner.")

name = guests[1].title()
print(name + ",please come to dinner.")

del(guests[0])
del(guests[0])

print(guests)