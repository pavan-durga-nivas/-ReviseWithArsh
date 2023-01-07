nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_count = int(input())
sum_nums = int(input())
list_digit = []
i = 0
r = 0
multiplier = 0
set_value = []
while i < number_count:
    multiplier += 10**i
    i += 1

first_check = multiplier*1
last_check = multiplier*9
# Function Definition


def sum_check(num):
    sum_2 = 0
    list_digit = []
    r = 0
    while num > 0:
        digit = num % 10
        list_digit += [digit]
        sum_2 += digit
        if digit == 0:
            r += 1
            break
        num /= 10
        num = int(num)
    return sum_2, list_digit, r


for j in range(first_check, last_check+1):
    sum_1, list_dig_1, r1 = sum_check(j)
    set_check = set(list_dig_1)
    if sum_nums == sum_1 and (list_dig_1 not in set_value) and (len(set_check) == len(list_dig_1)) and (r1 == 0):
        set_value += [list_dig_1]
new_set_value = []

for z in set_value:
    z.sort()
    if z not in new_set_value:
        new_set_value += [z]

print(new_set_value)
