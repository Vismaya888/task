n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
*
**
***
****
*****
"""
n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("*",end="")
    print()

"""
*****
****
***
**
*


Git is a free, open source version control tool that 
developers install locally on their personal computers,
while GitHub is a pay-for-use online service built to run Git in the cloud.
"""

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

"""
12345
1234
123
12
1

"""
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

"""
1
12
123
1234
12345
"""

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(2,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

"""
12345
1234
123
12
1
12
123
1234
12345

"""