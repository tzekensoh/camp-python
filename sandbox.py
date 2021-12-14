# Using variables. Choose meaningful names
from microbit import *
name = "Wendy"
feeling = "happy"
display.scroll(name + " is " + feeling)

# Math
from microbit import *
yearBorned = 1972
yearCurrent = 2021
age = yearCurrent - yearBorned
display.scroll("My age is " + str(age)) # try without str

# Boolean
from microbit import *
yearBorned = 2011
yearCurrent = 2021
age = yearCurrent - yearBorned
isPreteen = (age >= 9) and (age <= 12) 
display.scroll("Am I a preteen? " + str(isPreteen)) 

# Math: must use ** and % to come up with 333
# e.g. # (2**10 + 309) % 1000
from microbit import *
magicNumber = 1+1 
display.scroll(magicNumber)

# List and Loops
from microbit import *
favoriteAnimals = ['giraffe', 'zebra', 'lion', 'panda']
display.scroll("my most favorite animal is " + favoriteAnimals[0])
# del favoriteAnimals[0]
# change text to my other favorite animals are
display.scroll("my favorite animals are: ")
for animal in favoriteAnimals:
    display.scroll(animal)
