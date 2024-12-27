x=int(input())
temp=[]
match x:
    case 0:
        y=int(input("Enter a number:"))
        while(y>1):
            reminder=y % 2
            temp.append(reminder)
            y=y//2
        if (y==0):
            temp.append(0)
        else:
            temp.append(1)
    case 1:
        y=int(input("Enter a number:"))
        while(y>1):
            reminder=y % 8
            temp.append(reminder)
            y=y//8
        if(y>0):
            temp.append(y)
        else:
            temp=temp
    case 2:
        y=int(input("Enter a number:"))
        while(y>1):
            remainder=y % 16
            match remainder:
                case 10:
                    temp.append("A")
                case 11:
                    temp.append("B")
                case 12:
                    temp.append("C")
                case 13:
                    temp.append("D")
                case 14:
                    temp.append("E")
                case 15:
                    temp.append("F")
                case _:
                    temp.append(remainder)
            y=y//16
        if(10>y>0):
                temp.append(y)
        elif(16>y>9):
            match y:
                case 10:
                    temp.append("A")
                case 11:
                    temp.append("B")
                case 12:
                    temp.append("C")
                case 13:
                    temp.append("D")
                case 14:
                    temp.append("E")
                case 15:
                    temp.append("F")
        else:
            temp=temp
    case 3:
        a=[]
        b=[]
        y=int(input("Enter binary number:"))
        while (y>0):
            a.append(y%10)
            y=y//10
        for i in range (len(a)):
            b.append(a[i]*2**i)
        temp.append(sum(b))
temp.reverse()
for i in temp:
    print(i,end="")