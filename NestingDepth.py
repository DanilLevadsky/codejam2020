def solution():
    arr = list(input())
    for x in range(len(arr)):
        for _ in  range(int(arr[x])):
            temp = "(" + arr[x] + ')'
            arr[x] = temp
    string = ''.join(arr)
    while string.find(')(') != -1:
        string = string.replace(")(", "")
    return string    
    
    
T = int(input())
for x in range(1, T + 1):
    res = solution()
    print(f"Case #{x}: {res}")
