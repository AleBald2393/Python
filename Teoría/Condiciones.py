# Condition Equal

a = 5
a == 6

# Greater than Sign

i = 6
i > 5

# Greater than Sign

i = 2
i > 5

# Inequality Sign

i = 6
i != 6

# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example

age = 18
# age = 19

if age > 15:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
