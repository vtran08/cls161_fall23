# Exercise 3-1

friends = ['Yao', 'Serafina', 'Justyn', 'Cerena']

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])

# Exercise 3-2

message = "I miss you, "

print(message + friends[0])
print(message + friends[1])
print(message + friends[2])
print(message + friends[-1])

# Exercise 3-3 (Note: Using artists instead of mode of transportation)

artists = ['Sarah Sze', 'Carl Andre', 'Mickalene Thomas']

print("\n")
print("I am a fan of " + artists[0])
print(artists[1] + " is a sculptor")
print(artists[-1] + " is an interdisciplinary artist")

# Exercise 3-4 

guests = ['Kim Namjoon', 'Tavares Strachan', 'Sarah Sze']

message = ", you are invited to dinner at my place!"

print("\n")
print(guests[0] + message)
print(guests[1] + message)
print(guests[-1] + message)

# Exercise 3-5

del guests[0]
guests.insert(0, "Min Yoongi")
print("\n" + guests[0] + message)
print(guests[1] + message)
print(guests[-1] + message)
print("Unfortunately, Kim Namjoon could not make it")

# Exercise 3-6

guests.insert(0, "Lisa Sigal")
guests.insert(2, "Darin Murphy")
guests.append("Carrie Salazar")

print("\n" + guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print(guests[3] + message)
print(guests[4] + message)
print(guests[-1] + message)
print("We found a bigger table!")

# Exercise 3-7

guest1 = guests.pop(-1)
print("I'm sorry, " + guest1 + " there is not enough room for you at the dinner :(")

guest2 = guests.pop(-1)
print("I'm sorry, " + guest2 + " there is not enough room for you at the dinner :(")

guest3 = guests.pop(-1)
print("I'm sorry, " + guest3 + " there is not enough room for you at the dinner :(")

guest4 = guests.pop(-1)
print("I'm sorry, " + guest4 + " there is not enough room for you at the dinner :(")

print("Oof, sorry I can actually only have 2 people over")




