n = int(input("qani kilo es?  "))


l = str(input("qani kilo ches?  "))
k=[]
dinozavr = l.split(" ")

for i in l:
    k.append(int(i))

print(k)

t = tuple(dinozavr)

print(t)
