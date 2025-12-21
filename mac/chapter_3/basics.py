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
Notice the thing the function returns is denoted by the return keyword
"""
def add(a, b):
    result = a + b
    return result

"""
You can call a function by using the function name
and passing in the arguments, you can set the returned result to a variable
"""
x = add(1, 2)
print(x)

"""
Control flow lets you do something based on a condition
Try to guess what the output will be before you run the code
"""
if True:
    print("True")
else:
    print("False")

"""
Certain operations will return truth value like comparisons
which you can use in control flow
"""
if 2 < 1:
    print("1 is greater than 2")
else:
    print("1 is not greater than 2")

"""
You can also use variables in your comparisons
"""
a = 1
b = 2
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

"""
Here are some other comparison operators:
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""

"""
Lastly we should go over loops
loops let you iterate over a list and do something on
each item
"""
l = [1, 2, 3]
for x in l:
    print(x * 2)

"""
Okay last one for real, the dictionary data type
This lets you map a key to a value
"""
d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(d)
if "key1" in d:
    print(f"key1 is in the dictionary as {d['key1']}")

if "key4" in d:
    print("key4 is in the dictionary")
else:
    print("key4 is not in the dictionary")
 
"""
--------------------------------
Exercises:
--------------------------------
"""

"""
1. Write a function that takes in a codon and returns the amino acid
Given the following codon to amino acid dictionary
Dont forget the return keyword
"""
codon_to_amino_acid_dict = {
    "AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAT": "N",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACT": "T",
    "AGA": "R",
    "AGC": "S",
    "AGG": "R",
    "AGT": "S",
    "ATA": "I",
    "ATC": "I",
    "ATG": "M",
    "ATT": "I",
    "CAA": "Q",
    "CAC": "H",
    "CAG": "Q",
    "CAT": "H",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCT": "P",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGT": "R",
    "CTA": "L",
    "CTC": "L",
    "CTG": "L",
    "CTT": "L",
    "GAA": "E",
    "GAC": "D",
    "GAG": "E",
    "GAT": "D",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCT": "A",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGT": "G",
    "GTA": "V",
    "GTC": "V",
    "GTG": "V",
    "GTT": "V",
    "TAA": "*",
    "TAC": "Y",
    "TAG": "*",
    "TAT": "Y",
    "TCA": "S",
    "TCC": "S",
    "TCG": "S",
    "TCT": "S",
    "TGA": "*",
    "TGC": "C",
    "TGG": "W",
    "TGT": "C",
    "TTA": "L",
    "TTC": "F",
    "TTG": "L",
    "TTT": "F",
}

def codon_to_amino_acid(codon):
    ### Your code here ###
    pass # remove this line and write your code here
 

# This should print "K"
print(codon_to_amino_acid("AAA"))

"""
2. Use the previous function to write a function
that takes in a list of codons and returns a list of amino acids.
You will need to use the append method to add the amino acids to the result list.
You can do result.append(something) to add something to the result list.
"""
def codons_to_amino_acids(codons):
    result = []
    ### Your code here ###

# This should print ["H", "G", "F"]
print(codons_to_amino_acids(["CAT", "GGA", "TTC"]))

"""
3. Write a function that takes in a string of DNA and returns
the corresponding Protein sequence. You will need the split_in_n function
I've written for you to split a string into a list of strings of length n.
Additionally you will need to use the join method to join a list of into a single string. 
You can you it like this:
"".join([1, 2, 3]) -> this will return "123" 
where "" is the thing that goes between the elements of the list.
"-".join([1, 2, 3]) -> will return "1-2-3"
since this time I joined on "-"
"""

def split_in_n(sequence, n):
    result = []
    for i in range(0, len(sequence), n):
        result.append(sequence[i:i+n])
    return result

def dna_to_protein(dna):
    result = []
    ### Your code here ###

# This should print "MADLFKDAIEFELTKWDL"
print(dna_to_protein("ATGGCTGACCTGTTCAAGGACGCTATCGAGTTCGAGCTGACCAAGTGGGACCTG"))