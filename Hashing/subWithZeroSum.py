'''Program for Sub array with zero sum!'''
def subArrayWithZeroSum(arr):
    preSum=0
    h=set()
    for i in arr:
        preSum+=i
        if preSum==0:
            return True
        elif preSum in h:
            print(h)
            return True
        h.add(preSum)
    return False           


arr=list(map(int,input().split()))
print(subArrayWithZeroSum(arr))
