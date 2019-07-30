### set set set set
# Sets are unordered collections of distinct hashable objects.
# sets can be use for inmutable objects but not for mutable objects like
# mutable objects: list and dictionaries
# inmutable objects: tuple, string, range
# types of set:
#       Set        (is mutable)
#       Frozen Set (is not mutable after it was created)
#key idea:
#       sets cannot be indexed (no locations)
#       object in the set are unique or distinct (you can't duplicated any element)
# useful for: keeping track of distinct objects
# and doing mathematical set operations like unions, intersections and set difference

ids = set()        # empty set
ids = set([1,2,3,4,5,6,7,8])
print(len(ids))
print(dir(set))    #check all the attributes available of a set

ids.add(10)
print(ids)
ids.add(2)      # this object is already in the set, therefore it will not duplicate it.
print(ids)
print(ids.pop())       #return an arbitrary member of the set and takes it from the set
print(ids.pop())       #return an arbitrary member of the set and takes it from the set
print(ids.pop())       #return an arbitrary member of the set and takes it from the set
print(ids)

idss = set(range(10))
print(idss)
males = set([1,3,4,7,9])
females = idss - males
print(type(females))
print(females)

#set union
everyone =  males | females
print(everyone)
#set intersection
print(everyone & set([1,2,3,8,11,13,15]))


word = "asatjgequhsanfdutasfjkjauitjafljhuwhjdnfjabhuhertnjsdf"
letters=set(word)
print(len(letters))     #number of unique letter in word