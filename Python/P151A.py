# A - Soft Drinking

n, k, l, c, d, p, nl, np = [int(i) for i in input().split()]
print(int(min(k*l/nl,c*d,p/np)/n))