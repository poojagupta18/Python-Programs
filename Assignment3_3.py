def Min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if( min > arr[i]):
            min = arr[i]
    return min       
        
    
def AddNumbersInList(numOfElements):
    arr = list()
    for i in range(0, numOfElements):
        number = int(input())
        arr.append(number)
    return arr

a = int(input("Number of Elements:"))
arr = AddNumbersInList(a)
print(Min(arr))
