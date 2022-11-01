guests = ["kareem", "siraj", "amaan"]

name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, "waleed")

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")