num_list = [1, 2, 1, 2, 3, 5, 5, 1, 8, 9, 1]

counter = 0
index = 0
for num in num_list:
    for num2 in num_list[index +1:]:
        if num is num2:
            counter += 1
        index += 1 
return counter
