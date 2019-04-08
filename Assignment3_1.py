#Addition of Elements in the list

def AddInList(numOfElement):
    arr = list()
    for i in range(0, numOfElement):
        number = int(input())
        arr.append(number)
    return arr   

def Addition(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum   
        

a = int(input( "Number of Elements: " ))
arr = AddInList(a)
print(Addition(arr))
