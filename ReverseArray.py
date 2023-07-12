array = list(map(int,input().strip().split()))
length = len(array)
for i in range(length//2):
    temp = array[i]
    array[i] = array[length - 1 - i]
    array[length - 1 - i] = temp
print(array)