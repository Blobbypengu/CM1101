a = ["tree", "sheep", "horse"]
b = ["cow", "tree", "moose", "sheep", "aubergine", "horse"]
c = set(a)
d = [x for x in b if not x in c]
print(d)