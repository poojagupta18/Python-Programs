from MarvellousNum import *

def AddNumbersInList(numOfElements):
    arr = list()
    for i in range(0, numOfElements):
        number = int(input())
        arr.append(number)
    return arr

#addition Of Primes
def ListPrimes(primeList):
    sum = 0
    for i in range(0, len(primeList)):
        sum += primeList[i]
    return sum    


a = int(input("Number of Elements : "))
arr = AddNumbersInList(a)
primeList = list()

for i in range(0, len(arr)):
    if(ChkPrime(arr[i]) == 1):
        primeList.append(arr[i])
        
#print("primeList = " ,primeList)
        
print(ListPrimes(primeList))
