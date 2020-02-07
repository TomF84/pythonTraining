from sys import argv
from os.path import exists
# First we gather the name of the script and input that is supposed to be a file in cwd
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these on one line, how? indata = open(from_file, 'r') or open(from_file).read() ?

#in_file = open(from_file)
indata = open(from_file).read() #indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

print(f"Does the ouput file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

#print("Allright, all done")

#out_file.close()
#in_file.close()