def CalculateFrequency(arr, key):
    count = 0;
    for i in range(0, len(arr)):
        if( arr[i] == key ):
            count = count + 1
    return count        
        
def AddNumbersInList(numOfElements):
    arr = list()
    for i in range(0, numOfElements):
        number = int(input())
        arr.append(number)
    return arr

a = int(input("Number of Elements : "))
arr = AddNumbersInList(a)
b = int(input("Element to search :"))
print(CalculateFrequency(arr, b))
