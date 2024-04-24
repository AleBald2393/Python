for val in sequence:
      # statement(s) to be executed in sequence as a part of the loop.


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)

for number in range(1, 11):
    print(number)

for number in range(11):
    print(number)

for number in range(1, 11):
    print(number)

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

while condition:
    # Code to be executed while the condition is true
    # Indentation is crucial to indicate the scope of the loop

  count = 1
while count <= 10:
    print(count)
    count += 1
      
# Use the range

range(3)

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

UN LOOP POR EJEMPLO PARA MULTIPLICAR
# Write your code here
i=0
for i in range (0,11):
    print (f"6x{i}= {6*i}")
    i=i+1
j=0
for j in range (0,11):
    print (f"7x{j}= {7*j}")
    j=j+1

      # Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

print("Multiplication table of 6:")
for i in range (10):
    print("6*",i,"=",6*i)
print("Multiplication table of 7:")
for i in range (10):
    print("7*",i,"=",7*i)
