x=int(input())
temp=[]
match x:
    case 0:
        y=int(input("Enter a number:"))
        while(y>1):
            reminder=y % 2
            temp.append(reminder)
            y=y//2
        if ((y/2)==0):
            temp.append(0)
        else:
            temp.append(1)
        temp.reverse()
        for i in temp:
            print(i,end="")
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
        temp.reverse()
        for i in temp:
            print(i,end="")