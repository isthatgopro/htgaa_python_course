"""
Print statements let you print to the console
print("something")
Useful for seeing the output of your code
"""
print("Python Basics")

"""
Variables let you store data and use it later
"""
x = 1
y = 2

"""
You can print a variable
"""
print(x)

"""
You can add variables together and 
store them in another variables
"""
z = x + y 
print(z)

"""
A lot of things can be stored in variables
Here are some other examples: sentences and lists
"""
sentence = "Hello World"
numbers = [1, 2, 3, 4, 5]
print(sentence)
print(numbers)

"""
Things that have length like strings and lists can be used
With the built in len function to get the length
"""
print(len(sentence))
print(len(numbers))

"""
Now you know 2 built in functions: print and len
These take in one argument and do something with it.
But what if you want to write your own functions?
You can do that by defining a function with the def keyword.
"""
def add(a, b):
    return a + b

"""
You can call a function by using the function name
and passing in the arguments
"""
x = add(1, 2)
print(x)

"""
Lastly we should go over loops
loops let you iterate over a list and do something on
each item
"""
l = [1, 2, 3]
for x in l:
    print(x * 2)