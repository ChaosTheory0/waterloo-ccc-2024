n = int(input())
arr_a = input().split(' ')
arr_b = input().split(' ')
for i in range(n):
    arr_a[i] = int(arr_a[i])
    arr_b[i] = int(arr_b[i])

for i in range(n):
    for j in range(1, n - 1):
        print(j)
       
 
if arr_a == arr_b:
    print('YES')
    print(0)
