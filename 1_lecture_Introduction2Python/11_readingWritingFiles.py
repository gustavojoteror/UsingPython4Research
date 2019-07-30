#

########################
# READING A FILE
filename = 'read.txt'

for line in open(filename):  #open("name") created a file object and then we loop over file object using a for loop
    print(line)               # line consists of everything "gola line\n", even the \n
    line= line.rstrip()      # rstrip() takes the \n from what it reads
    line= line.split(' ')    # split() returns a list if what ever the line is splitted into

    print(line)


########################
# writing A FILE
file= open('write.txt', 'w')    # first argument is the name of the file, the second is what we want to do with that
# the above line creates an object file
file.write('Python\n')        # a method of the object file is write()
file.write('is\n')
file.write('writing')
file.close()