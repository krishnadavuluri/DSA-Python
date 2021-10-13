'''Program for subarray with given sum!'''
def subArrayWithGivenSum(arr,Sum):
    preSum=0
    Set=set()
    for i in arr:
        preSum+=i
        if preSum==Sum:
            return True
        if preSum-Sum in Set:
            return True
        Set.add(preSum)        
    return False

arr=list(map(int,input().split()))
Sum=int(input())
print(subArrayWithGivenSum(arr,Sum))