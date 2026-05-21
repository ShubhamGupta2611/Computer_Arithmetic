def comapare(a,b):
    if a=="1" and b=="0":
        #as -1 is of length 2 so the string will be formated wrong hence used 2 instead of -1
        return "2"
    elif a=="0" and b=="1":
        return "1"
    else:
        return "0"
def twos(a):
    ans=""
    for i in a:
        if (i=="0"):
            ans+="1"
        else:
            ans+="0"
    ans=format(int(ans,2)+1,f'0{len(a)}b')
    return ans
def adder(a, m):
    ans = ""
    c = 0    
    for i in range(len(m)-1, -1, -1):
        if(a[i]=='1' and m[i]=='1' and c==0):
            ans="0"+ans
            c=1
        elif(a[i]=='1' and m[i]=='1' and c==1):
            ans="1"+ans
            c=1
        elif((a[i]=='1' or m[i]=='1') and c==0):
            ans="1"+ans
            c=0
        elif((a[i]=='1' or m[i]=='1') and c==1):
            ans="0"+ans
            c=1
        elif(a[i]=='0' and m[i]=='0' and c==0):
            ans="0"+ans
            c=0
        else:
            ans="1"+ans
            c=0
    return ans,c
def binary():
    n=int(input("for unsigned press 1 and for signed press 2:"))
    #binary multiplication of unsigned number by taking help of it's circuit diagram
    if(n==1):
        Q=int(input("enter the multiplier:"))
        M=int(input("enter the multiplicand:"))
        
        a="0000"
        q=format(Q,"04b")
        m=format(M,"04b")
        for i in q[::-1]:
            if(i=="0"):
                a,c=adder(a,"0000")
                
            else:
                a,c=adder(a,m)
            d=a[-1]
            q=q[:-1]
            a=a[:-1]
            q=d+q
            a=str(c)+a
        print("answer in binary",a+q)
        print("answer in integer",int(a+q,2))
    #binary multiplication of signed number by using by hand method
    else:
        Q=int(input("enter the multiplier:"))
        M=int(input("enter the multiplicand:"))
        q=format(abs(Q),"05b")
        m=format(abs(M),"05b")
        if(Q<0):
            q=twos(q)
        if(M<0):
            q,m,Q,M=twos(m),q,M,Q
        arr=[]

        for i in range(len(q)):
            if m[i]=="0":
                b=format(0,"010b")
            else:
                b="1"*(i+1)+q+"0"*(5-i-1)
            arr.append(b)
            c=0
            ans=""
        for i in range(10):
            d=sum([c,int(arr[0][9-i]),int(arr[1][9-i]),int(arr[2][9-i]),int(arr[3][9-i]),int(arr[4][9-i])])
            k=format(d,"05b")
            ans=k[-1]+ans
            k=k[:-1]
            c=int(k,2)
        print("answer in binary:",ans)
        print("answer in integer",int(twos(ans),2)*-1)
def booth():
    Q=int(input("enter the multiplier:"))
    M=int(input("enter the multiplicant:"))
    if Q == 0 or M == 0:
        print("answer in binary: 0000000000")
        print("answer in integer 0")
        return
    q=format(abs(Q),"05b")
    m=format(abs(M),"05b")
    if(Q<0 and M<0):
        pass
    elif(Q<0):
        m,q,M,Q=twos(q),m,Q,M
    elif(M<0):
        m=twos(m)
    arr=[]
    c="0"
    l=list()
    for i in range(len(m)):
        d=m[len(m)-i-1]
        l.insert(0,comapare(d,c))
        c=d
    m="".join(l)
    for i in range(len(q)):
        if m[i]=="0":
            b=format(0,"010b")
        elif m[i]=="1":
            b=format(abs(Q<<len(q)-i-1),"010b")
        else:
            b="1"*(i+1)+twos(q)+"0"*(len(q)-i-1)
        arr.append(b)
        c=0
        ans=""
    for i in range(10):
        d=sum([c,int(arr[0][9-i]),int(arr[1][9-i]),int(arr[2][9-i]),int(arr[3][9-i]),int(arr[4][9-i])])
        k=format(d,"05b")
        ans=k[-1]+ans
        k=k[:-1]
        c=int(k,2)
    print("answer in binary:",ans)
    if (M<0)^(Q<0):
       print("answer in integer",int(twos(ans),2)*-1)
    else:
        print("answer in integer",int(ans,2))
def restoring():
    #taking idea for it's circuit diagram
    Q=int(input("Enter the Dividend"))
    M=int(input("Enter the Divisor"))
    q=format(Q,"b")
    m=format(M,"b")
    m="0"+m
    tm=twos(m)
    a="0"*len(m)
    ans=""
    for i in q:
        a=a[1:]
        a=a+i
        a,c=adder(a,tm)
        if a[0]=="1":
            a,c=adder(a,m)
            ans=ans+"0"
        else:
            ans=ans+"1"
    print("Quotient in binary:",ans)
    print("Quotient in integer",int(ans,2))
    print("Remainder in binary:",a)
    print("Remainder in integer",int(a,2))
def non_restoring():
    Q=int(input("Enter the Dividend"))
    M=int(input("Enter the Divisor"))
    q=format(Q,"b")
    m=format(M,"b")
    m="0"+m
    tm=twos(m)
    a="0"*len(m)
    ans=""
    if(Q>=M):
        for i in q:
            if a[0]=="1":
                a,c=adder(a[1:]+i,m)
            else:
                a,c=adder(a[1:]+i,tm)
            if a[0]=="1":
                ans+="0"
            else:
                ans+="1"
        if a[0]=="1":
            a,c=adder(a,m)
    else:
        ans="0"
        a=q
    print("Quotient in binary:",ans)
    print("Quotient in integer",int(ans,2))
    print("Remainder in binary:",a)
    print("Remainder in integer",int(a,2))
while True:
    print("\n===== Computer Arithmetic Algorithms =====")
    print("1. Binary Multiplication")
    print("2. Booth Multiplication")
    print("3. Restoring Division")
    print("4. Non-Restoring Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        binary()

    elif choice == "2":
        booth()

    elif choice == "3":
        restoring()

    elif choice == "4":
        non_restoring()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")              
