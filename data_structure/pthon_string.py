# # List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.

# # Mutable: list elements can be changed, updated, added, or removed after the list is created.
# # Ordered: elements maintain the order in which they are inserted.
# # Index-based: elements are accessed using their position, starting from index 0.

# 1. Using Square Brackets: Square brackets [] are used to create a list directly.
a = [1, 2, 3]
print(a)

# 2. Using list() Constructor: A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor.
a= list((1,2,3,'apple',4.5))
print(a)
b = list("gfg")
print(b)

# 3. Creating List with Repeated Elements: A list with repeated elements can be created using the multiplication (*) operator.
a = [2] * 5
b = [0] * 7
print(a)

# 1. append(): Adds an element at the end of the list.
a = [1, 2]
a.append(3)
print(a)

# 2. insert(): Adds an element at a specific position.
a.insert(1,2)
print(a)

# 3. extend(): Adds multiple elements to the end of the list.
a.extend([3, 4])
print(a)

# 1. remove(): Removes the first occurrence of an element.
a.remove(2)
print(a)

# 2. pop(): Removes the element at a specific index or the last element if no index is specified.
a= [1,2,3]
a.pop()
print(a)

# 3. del statement: Deletes an element at a specified index.
del a[1]

# 4. clear(): removes all items.
a.clear()
