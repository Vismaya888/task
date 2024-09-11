lim = int(input("Enter the limit of First list : "))

lis1=[]
lis2=[]
for _ in range(1,lim+1):
    ele1 = int(input("Enter the elements of first list : "))
    lis1.append(ele1)
lim2 = int(input("Enter the limit of second list : "))
for _ in range(1,lim2+1):
    ele2 = int(input("Enter the elements of second list : "))
    lis2.append(ele2)
print(f'First List : {lis1}')
print(f'Second List : {lis2}')
for i in range (0,len(lis1)):
    for j in range(i+1,len(lis1)):
        if lis1[i]>=lis1[j]:
            lis1[i],lis1[j]==lis1[j],lis1[i]
print("Sorted List1",lis1)
for i in range(0,len(lis2)):
    for j in range(i+1,len(lis2)):
        if lis2[i]>=lis2[j]:
            lis2[i],lis2[j]=lis2[j],lis2[i]
print("Sorted List2 ",lis2)
lis3=lis1+lis2
for i in range(0,len(lis3)):
    for j in range(i+1,len(lis3)):
        if lis3[i] >= lis3[j]:
            lis3[i],lis3[j] = lis3[j],lis3[i]
print("Sorted List", lis3)    
