# take an existing list and apply soe operation to all of the items on the list and then
# create a new list that contains the results

numbers  = range(10)
squares = []

# normal way
for i in numbers:
    j = i**2
    squares.append(j)

print(squares)

#with list comprehention
squares2 = [i**2 for i in numbers]  # are very fast and elegant
print(squares2)

print(squares == squares2)