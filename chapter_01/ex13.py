from sys import argv
# read the WYSS section for how to run this
script, first, second, third, log = argv
extra = input('What else do we need?')

with open(log, 'w') as f:
    f.write("The script is called: {}\n".format(script))
    f.write("Your first variable is: {}\n".format(first))
    f.write("Your second variable is: {}\n".format(second))
    f.write("Your third variable is: {}\n".format(third))
    f.write("Your extra variable is: {}\n".format(extra))
