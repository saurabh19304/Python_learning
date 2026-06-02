# Syntax: open(file_name, mode) 
# Parameters:
# file_name: This parameter as the name suggests, is the name of the file that we want to open.
# mode: This parameter is a string that is used to specify the mode in which the file is to be opened. The following strings can be used to activate a specific mode:
# "r": This string is used to read(only) the file. It is passed as default if no parameter is supplied and returns an error if no such file exists.
# "w": This string is used for writing on/over the file. If the file with the supplied name doesn't exist, it creates one for you.
# "a": This string is used to add(append) content to an existing file. If no such file exists, it creates one for you.
# "x": This string is used to create a specific file.
# "b": This string is used when the user wants to handle the file in binary mode. This is generally used to handle image files.
# "t": This string is used to handle files in text mode. By default, the open() function uses the text mode.

f = open("geek.txt", "r")
print(f)
print("filename:", f.name)
print("mode:", f.mode)
print("is closed?", f.closed)

#reading file 
content = f.read()
print(content)

f.close()
print("is closed?" , f.closed)


#writing in file 
# Writing to a file is done using the mode "w". This creates a new file if it doesn’t exist, or overwrites the existing file if it does. The write() method is used to add content. After writing, make sure to close the file.
with open("geek.txt", "w") as file:
  file.write("Hello, pyhton!\n")
  file.write("hello handling is easy with python.")

# "w" mode opens the file for writing (overwrites existing content if the file already exists).
# write() method adds new text to the file.
# When using with, the file closes automatically at the end of the block.

print("file written successfully")


# #handling exception when clsing a file
#  It's important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations. Here, the finally block ensures the file is closed even if an error occurs.

try:
  file = open("geek.txt", "r")
  constent = file.read()
  print(content)
except FileNotFoundError as e:
  print("Error:", e)
finally:
  file.close()