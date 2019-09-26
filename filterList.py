list = [1,2,3,6,9,11,13,15,67]

def filterUnderTen(array):
    underTen = []
    for ele in array:
        if ele < 10 :
            underTen.append(ele)
    return underTen


print(filterUnderTen(list))