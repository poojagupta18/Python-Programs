def Max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if( max < arr[i] ):
            max = arr[i]
    return max        
        
    
def AddNumbersInList(numOfElements):
    arr = list()
    for i in range(0, numOfElements):
        number = int(input())
        arr.append(number)
    return arr

a = int(input("Number of Elements:"))
arr = AddNumbersInList(a)
print(Max(arr))

    
