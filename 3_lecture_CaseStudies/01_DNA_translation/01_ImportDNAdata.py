inputfile = 'dna.txt'
f         = open(inputfile, 'r')    #r for reading
seq       =  f.read()           #we read the whole file at once

print(seq)      # the sequence is printed including line breaks which means there is a character: \n in the sequence
# let's use the replace method
seq = seq.replace('\n', '')   # a string is immutable, therefore we need to assign it to a variable
print(seq)       # now there are no line breaks
seq = seq.replace('\r', '')   # \r is a carriage return
# \n is new line
# \t is a tab
# \r is a carriage return


# another way of reading the file

with open(inputfile, 'r') as f:     # compound statement
    seq = f.read()

