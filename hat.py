n = int(input())
h = []
matching = 0
for i in range(n):
    h.append(int(input()))

for i in range(int(n / 2)):
    if h[i] == h[i + int(n/2)]:
       matching += 2 

print(matching)

