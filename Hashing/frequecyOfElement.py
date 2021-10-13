'''Counting Frequency of elements'''
array=list(map(int,input().split()))
Set=set()
for i in array:
    Set.add(i)
print(len(Set))    