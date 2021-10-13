'''Program for parenthesis checker'''
dic={"}":"{",")":"(","]":"["}
parren=input()
stack=[]
flag=0
for i in parren:
    if i not in dic:
        stack.append(i)
    else:
        if len(stack)!=0:
            if dic[i]==stack[len(stack)-1]:
                stack.pop()
            else:
                flag=1
                break
        else:
            flag=1
            break
if flag==0:
    print("Balanced")
else:
    print("Unbalanced")