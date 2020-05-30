
def remove_dup(arr):
    if len(arr) <= 1:
        return
    
    prev = 0
    idx = 1
    
    while idx < len(arr):
        if len(arr) <= 1:
            break
        elif arr[prev] == arr[idx]:
            arr.pop(idx)
        else:
            prev = idx
            idx += 1

x = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6]
remove_dup(x)
print(x)

