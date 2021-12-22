# Using variables. Choose meaningful names
name = "Wendy"
feeling = "happy"
basic.show_string(name + " is " + feeling)

# Math
yearBorned = 1972
yearCurrent = 2021
age = yearCurrent - yearBorned
basic.show_string("My age is " + str(age)) # try without str

# Boolean
yearBorned = 2011
yearCurrent = 2021
age = yearCurrent - yearBorned
isPreteen = (age >= 9) and (age <= 12) 
basic.show_string("Am I a preteen? " + str(isPreteen)) 

# Math: must use ** and % to come up with 333
# e.g. # (2**10 + 309) % 1000
magicNumber = 1+1 
basic.show_number(magicNumber)

# List and Loops
favoriteAnimals = ['giraffe', 'zebra', 'lion', 'panda']
basic.show_string("my most favorite animal is " + favoriteAnimals[0])
# del favoriteAnimals[0]
# change text to my other favorite animals are
basic.show_string("my favorite animals are: ")
for animal in favoriteAnimals:
    basic.show_string(animal)
