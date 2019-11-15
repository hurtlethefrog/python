numbers = [1, 2, 3, 4, 5]
days = ['mon', 'tues', 'wed']

squared_list = [n*n for n in numbers]

print(squared_list)

date_dict = {num: day for num, day in zip(numbers, days)}

print(date_dict)