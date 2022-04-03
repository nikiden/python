cube = []
summ_1 = 0
summ_2 = 0
for i in range(1, 1001, 2):
        cube.append(i ** 3)

for number in cube:
    cube_summ = 0
    j = number
    while j:
        cube_summ += j % 10
        j = j // 10
    if cube_summ % 7 == 0:
        summ_1 += number

    number += 17
    cube_summ = 0
    j = number
    while j:
        cube_summ += j % 10
        j = j // 10
    if cube_summ % 7 == 0:
        summ_2 += number
print(summ_1)
print(summ_2)
