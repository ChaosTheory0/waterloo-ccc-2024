n = int(input())
arr_a = input().split(' ')
arr_b = input().split(' ')
can_be_swiped = False
is_right_swipe = True
for i in range(n):
    arr_a[i] = int(arr_a[i])
    arr_b[i] = int(arr_b[i])

if arr_a[0] != arr_b[0]:
    if arr_b[0] == arr_b[1]:
        can_be_swiped = True

if arr_a[1] != arr_b[1]:
    if arr_b[1] == arr_a[0]:
       is_right_swipe = False 
       can_be_swiped = True

arr_str = str(arr_a[0])
for i in range(1, n):
    arr_str += ' '
    arr_str += str(arr_a[i])

letter = 'L'
if is_right_swipe:
    letter = 'R'


if can_be_swiped:
    print(1)
    print(letter + ' ' + arr_str)
    
else:
    print('NO')
