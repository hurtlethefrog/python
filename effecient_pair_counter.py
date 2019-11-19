def pair(arr):

    nm = dict()

    for i in range(len(arr)):
        if arr[i] in nm.keys():
            nm[arr[i]] += 1
        else:
            nm[arr[i]] = 1

    ans = 0
    for val in nm:
        count = nm[val]
        ans += (count * (count - 1))
    return ans

print(pair([1,1,1,2,2,3,4,5,5,5,6,1]))