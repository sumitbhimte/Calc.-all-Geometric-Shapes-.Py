import statistics
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = statistics.mean(lst)

count = 0
for value in lst:
    if(value < K):
        count += 1

print(count)