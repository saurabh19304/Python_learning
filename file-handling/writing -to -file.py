# "w"	Write mode: creates file if missing, truncates (erases) if it exists
# "a"	Append mode: creates file if missing, writes data always at the end
# "x"	Exclusive create: creates new file, but fails with FileExistsError if it already exists
# "b"	Binary flag: used with other modes (e.g., "wb", "ab") for binary files
# # "+"	Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
# encoding=	Specify text encoding (e.g., "utf-8") when working with text files
# newline=	Control newline translation in text mode (e.g., "\n")

#overwriting an existing file 

with open("file.txt", "w", encoding='utf-8') as f:
  f.write("created using write mode. \n")
  f.write("second line. \n")

with open("file.txt", "r", encoding="utf-8") as f:
  print(f.read())

#append to an existing file 
with open("file.txt", "a", encoding="utf-8") as f:
  f.write("appended line. \n")
#"a" always writes at the end
with open("file.txt", "r", encoding="utf-8") as f:
  print(f.read())


# #create only if it does not exist 
#  This tries to create file.txt only if it doesn’t exist, otherwise prints an informative message.

try:
  with open("file.txt", "x", encoding="utf-8") as f:
    f.write("created using exclusive mode. \n")

except FileExistsError:
  print(" file.txt already exist, exclusve creation aborted.")

#writitng multiple line at once 
# Sometimes you need to write several lines at once instead of one by one. Python provides two common approaches: writelines() for lists of strings and join() for building a single text block.

lines = ["first line \n", "second line\n", "third line\n"]
with open("file1.txt", "w", encoding="utf-8") as f:
  f.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as f:
  print(f.read())

#more cleaner example
#join + single write 

lines = ["lineA", "lineB", "lineC"]
text = "\n".join(lines) + "\n"
with open("file2.txt", "w", encoding="utf-8") as f:
  f.write(text)

with open("file2.txt", "r", encoding="utf-8") as f:
  print(f.read())


#writin to binary file

# For non-text data (like images, audio, or other binary content), use binary write mode ("wb"). This treats the file as raw bytes instead of text.
#The following code writes a small sequence of bytes into a file called file.bin and then reads it back in binary mode.

data = b'\x00\x01\x02\x03\x04'
with open("file bin ", "wb") as f:
  f.write(data)
 