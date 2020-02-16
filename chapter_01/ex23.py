import sys
script, input_encoding, error = sys.argv

#This is the main script, it returns itselve?
def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line: # If the line is not empty, work on the line via the print_line function
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # This probably means that if the next line is empty we exit the main function and thus end the script!
        

def print_line(line, encoding, errors):
    next_lang = line.strip()# Removes spaces
    raw_bytes = next_lang.encode(encoding, errors=errors) #This encodes the line in utf-8 encoding
    cooked_string = raw_bytes.decode(encoding, errors=errors) #This decodes the line back to something that can be interpreted
    
    print(raw_bytes, "<===>", cooked_string)

# This opens the list and enforces the use of uft-8 encoding when reading the data.
languages = open("languages.txt", encoding="utf-8")

#This just kicks of the reading of the entire file, probably shorter than for line in file:
main(languages, input_encoding, error)
