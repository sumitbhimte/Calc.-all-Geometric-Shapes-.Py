def triangular_series( n ):
    j = 1
    k = 1

    for i in range(1, n + 1):
        print(k, end = ' ')
        j = j + 1 
        k = k + j

n = 5
triangular_series(n)