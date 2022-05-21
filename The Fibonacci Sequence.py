while True:
    pt2=0 
    pt1=1
    loop=0
    n=int(input("How many terms would you like to view? "))
    n=n-2
    if n>=0:
        print(str(pt2)+"\n"+str(pt1))
        t=pt2+pt1
        while loop<n:
            print(t)
            pt2=pt1
            pt1=t
            t=pt2+pt1
            loop=loop+1
    elif n==-2:
        pass
    elif n==-1:
        print("0")

