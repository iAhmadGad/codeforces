# A - Restoring Three Numbers

x  = [int(i) for i in input().split()]
x.sort()
print(x[3] - x[0], x[3] - x[1], x[3] - x[2])