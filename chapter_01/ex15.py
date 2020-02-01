from sys import argv
# First we gather the name of the script and input that is supposed to be a file in cwd
script, filename = argv
# Here we open the file that was used as argument to the script
txt = open(filename)
# Small message to inform that we will print the contents of the file.
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
