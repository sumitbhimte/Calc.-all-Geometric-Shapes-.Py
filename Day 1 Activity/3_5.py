list1 = ['24', '654', '74', '824']
list2 = ['424', '24', '74', '554']

set1 = set(list1)
set2 = set(list2)

missing = list(sorted(set1 - set2))
added = list(sorted(set2 - set1))

print('missing:', missing)
print('added:', added)