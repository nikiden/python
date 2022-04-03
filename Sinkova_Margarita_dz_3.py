percent_name = ['процент', 'процента', 'процентов']
for i in range(1, 101):
    if i >4 and i <20:
        print(i, ' ', percent_name[2])
    elif i%10 == 1:
        print(i,' ', percent_name[0])
    elif i%10 >=2 and i%10 <=4:
        print(i,' ', percent_name[1])
    else:
        print(i, ' ', percent_name[2])