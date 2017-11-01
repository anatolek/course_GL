m = 10
[print(*['{:>3}'.format(i*j) for j in range(1,m+1)]) for i in range(1,m+1)]