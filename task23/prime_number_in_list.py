limit = int(input("Enter the No. of elements you want insert : "))
lis1=[]
lis2=[]
lis3=[]
for _ in range(limit):
    ele = int(input("Enter the number : "))
    lis1.append(ele)
print(lis1)

for i in lis1:
    if i==2:
        lis3.append(i)
    elif i==1:
        lis2.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                lis2.append(i)
                break
            
            else:
                lis3.append(i)
                break
           
print(f'Prime {lis3}')
print(f'Non prime {lis2}')