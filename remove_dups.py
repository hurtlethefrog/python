numbers = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7]

output = []

def unique(arr):
    for num in arr:
        if not num in output:
            output.append(num)
    return output
print(unique(numbers))