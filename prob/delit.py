s = "this is a string"
l = list(s)  # convert to list
l[1] = ""    # "delete" letter h (the item actually still exists but is empty)
l[1:2] = []  # really delete letter h (the item is actually removed from the list)
del(l[1])    # another way to delete it
p = l.index("a")  # find position of the letter "a"
del(l[p])         # delete it
s = "".join(l)  # convert back to string
print (s)

oldstr= "Mama"
print (oldstr.replace("M", ""))

word = "Alex"
l= list(word)
l[2]=""
word= "".join(l)
print (word)