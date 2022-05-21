pt2=0
pt1=1
loop=0

n=int(input("How many terms would you like to view (must be > 1)? "))
n=n-2
print(pt2)
print(pt1)
t=pt2+pt1
while loop<n:
    print(t)
    pt2=pt1
    pt1=t
    t=pt2+pt1
    loop=loop+1
