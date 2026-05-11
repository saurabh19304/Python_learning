# Dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), values can be of any data type, whether mutable or immutable. This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.

data = {"name": "jake", "age": 22}
print(data)

b = dict(name="sam", age=20)
print(b)

# A value in a dictionary is accessed by using its key. This can be done either with square brackets [ ] or with the get() method. Both return the value linked to the given key.
d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()
# Note: Accessing a missing key with [ ] raises a KeyError, while get() is safer because it returns None (or a default value) instead of an error.

# Removing Dictionary Items
# Dictionary items can be removed using built-in deletion methods that work on keys:
# 1. del: removes an item using its key
d = {"a": 1, "b": 2}
del d["a"]
print(d)

# 3. popitem(): removes and returns the last inserted key-value pair
d = {"a": 1, "b": 2}
print(d.popitem())

# 4. clear(): removes all items from the dictionary
d = {"a": 1, "b": 2}
d.clear()
print(d)

# Iterating Through a Dictionary
d = {"a": 1, "b": 2}
for key in d:
    print(key)

d = {"a": 1, "b": 2}
for value in d.values():
    print(value)

d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)