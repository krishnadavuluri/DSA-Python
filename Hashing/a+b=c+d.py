'''Program to find atleast one combination a+b=c+d from the given list'''
arr=list(map(int,input().split()))
dic={}
flag=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        Sum=arr[i]+arr[j]
        if Sum not in dic:
            dic[Sum]=str(arr[i])+"+"+str(arr[j])
        else:
            print('{}={}+{}'.format(dic[Sum],arr[i],arr[j]))
            flag=1
            break
    if flag==1:
        break
if flag==0:
    print('No pairs found')    