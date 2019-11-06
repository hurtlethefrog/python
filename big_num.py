numbers = [1,2,3,4,5,6,23,50,1,2,9]

print(max(numbers))

# or long noob way

output = 0
for num in numbers:
    if num > output:
        output = num
print(output)