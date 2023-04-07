r=""
l = [*map(str, open(0))]
#print(l)
for w in l:
    if w =="\n":r+=" "
    else:r+=w[0]
    if w == ".\n":break
print(r)