def check_alternating(tested_str):
    letter_table = {}
    is_alternating = True
    count_list = []
    for letter in tested_str:
        if letter not in letter_table:
            letter_table[letter] = 1
        elif letter in letter_table:
            letter_table[letter] += 1

    for letter in tested_str:
        if letter_table[letter] > 1:
            count_list.append(1)
        else:
            count_list.append(0)

    for i in range(len(count_list) - 1):
        if count_list[i] == count_list[i + 1]:
            is_alternating = False
            break 
    return is_alternating



str_info = input().split(' ')
t = int(str_info[0])
lines = []

for i in range(t):
    lines.append(input())
for i in range(t):
    if check_alternating(lines[i]):
        print('T')
    else:
        print('F')


