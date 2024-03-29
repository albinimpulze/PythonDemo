# Dictionary





x = { "apple" : "a fruit" , "tomato" : "a vegetable" }
y = {"kung fu panda" : "is a movie", "Ferrari":"is a car"}
z = x.copy()
for key, value in y.items():
   z[key] = value
print(z)