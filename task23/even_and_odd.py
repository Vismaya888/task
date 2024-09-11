lis1=[]
lis2=[]

def even_odd(num):
    for i in range(1,num+1):
        ele = int(input("Enter the number : "))
        if ele%2==0:
            lis1.append(ele)
        else:
            lis2.append(ele)
    
    return lis1,lis2

n=int(input("Enter the limit : "))
even_odd(n)
print(f'Even : {lis1}')
print(f'Odd : {lis2}')