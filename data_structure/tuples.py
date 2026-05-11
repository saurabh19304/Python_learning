# A tuple is an immutable ordered collection of elements.

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
# Can hold elements of different data types.
# These are ordered, heterogeneous and immutable.

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

# Only tuples can be concatenated with tuples. Combining a tuple with other types like lists will raise an error. Tuples themselves can contain mixed datatypes.
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

# Slicing a tuple means creating a new tuple from a subset of elements of the original tuple. The slicing syntax is tuple[start:stop:step].

# Note: Negative Increment values can also be used to reverse the sequence of Tuples. 
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
# del tup
# print(tup)

# Tuple Unpacking with Asterisk (*)
# *operator is used in tuple unpacking to grab multiple items into a list. This is useful to extract just a few specific elements and collect the rest together.
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)