'''Program for stock span problem'''
l=list(map(int,input().split(" ")))
stack=[0]
print(1,end=" ")
for i in range(1,len(l)):
    f=0
    while stack and l[i]>l[stack[len(stack)-1]]:
        stack.pop()
        f=1
    if f==0:
        print(1,end=" ")
    else:
        if stack:
            print(i-stack[len(stack)-1],end=" ")
        else:
            print(i+1,end=" ")        
    stack.append(i)
                       
