n = int(input("Enter the limit for main list : "))
lis1 = []
lis2 = []
flag=0
for i in range(1,n+1):
    ele1 = int(input("Enter the elements of first list : "))
    lis1.append(ele1)

n2 = int(input("Enter the limit of sublist : "))
for i in range(1,n2+1):
    ele2 = int(input("Enter the element of sublist :"))
    lis2.append(ele2)

print(f'{lis1} and {lis2}')
for i in lis1:
    for j in lis2:
        if i==j:
            flag=1
if flag==1:
    print(True)
else:
    print(False)
            