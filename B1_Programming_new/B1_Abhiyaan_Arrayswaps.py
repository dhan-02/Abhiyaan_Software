def zeroes_first(Arr):
    
    swaps = 0
    count_one = 0

    for i in range(len(Arr)):
        if Arr[i] == 1:
            count_one += 1
        else:
            swaps += count_one
    return swaps
    
def ones_first(Arr):
    
    swaps = 0
    count_zero = 0
 
    for i in range(len(Arr)):
        if Arr[i] == 0:
            count_zero += 1
        else:
            swaps += count_zero
    return swaps

n = int(input("Enter n : "))
print("Enter values of array separated by space : ")
# Assume user enters n space separated values with 0's and 1's only
Arr = list(map(int,input().split()))
print("\nMin swaps required is ",min(ones_first(Arr),zeroes_first(Arr)))
