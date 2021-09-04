s='hrituj'
new=[]
for i, val in enumerate(s[:]):
    up=s[i].upper()
    c=s[:i] + up + s[i+1:]
    new.append(c)
print(new)