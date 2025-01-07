x=int(input())
temp=[]
table_3=['000','001','010','011','100','101','110','111']
table_4=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
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
        for i in a:
            if(0<=i<2):
                True
            else:
                raise ValueError("Every Number should be 0 or 1")
        for i in range (len(a)):
            b.append(a[i]*2**i)
        temp.append(sum(b))
    case 4:
        a=[]
        b=[]
        y=int(input("Enter octal number:"))
        while (y>0):
            a.append(y%10)
            y=y//10
        for i in a:
            if(0<=i<8):
                True
            else:
                raise ValueError("Every Number should be between 0 & 7")
        for i in range (len(a)):
            b.append(a[i]*8**i)
        temp.append(sum(b))
    case 5:
        y=input("Enter hexadecimal number:")
        a=[char for char in y]
        b=[None]*len(a)
        k=[]
        for i in a:
            if((i=="0"or i=="1"or i=="2"or i=="3"or i=="4"or i=="5"or i=="6"or i=="7"or i=="8"or i=="9"or i=="A"or i=="B"or i=="C"or i=="D"or i=="E"or i=="F")):
                True
            else:
                raise ValueError("Every Number should be between 0 & 9 and can have some alphabets like(A, B, C, D, E, F)")
        for i,c in enumerate(a):
            match c:
                case "A":
                    b[i]="10"
                case "B":
                    b[i]="11"
                case "C":
                    b[i]="12"
                case "D":
                    b[i]="13"
                case "E":
                    b[i]="14"
                case "F":
                    b[i]="15"
                case _:
                    b[i]=c
        for i in range (len(b)):
            b[i]=int(b[i])
        b.reverse()
        for i in range (len(b)):
            k.append(b[i]*16**i)
        temp.append(sum(k))
    case 6:
        a=[]
        groups=[]
        y=input("Enter binary number:")
        r_s=y[::-1]
        for i in range(0, len(r_s), 3):
            groups.append(r_s[i:i+3])  
        for group in groups:
            a.append(group[::-1])
        a=a[::-1]
        print(a)
        for i in range(len(a)):
            if(len(a[i])==3):
                for b in range(len(table_3)):
                    if (a[i]==table_3[b]):
                        temp.append(b)
            else:
                if (len(a[i])==2):
                    b='0'+a[i]
                    for i in range(len(table_3)):
                        if (b==table_3[i]):
                            temp.append(i)
                else:
                    b='00'+a[i]
                    for i in range(len(table_3)):
                        if (b==table_3[i]):
                            temp.append(i)
        temp.reverse()
    case 7:
        a=[]
        c=[]
        groups=[]
        y=input("Enter binary number:")
        r_s=y[::-1]
        for i in range(0, len(r_s), 4):
            groups.append(r_s[i:i+4])  
        for group in groups:
            a.append(group[::-1])
        a=a[::-1]
        print(a)
        for i in range(len(a)):
            if(len(a[i])==4):
                for b in range(len(table_4)):
                    if (a[i]==table_4[b]):
                        c.append(b)
            else:
                if (len(a[i])==3):
                    b='0'+a[i]
                    for i in range(len(table_4)):
                        if (b==table_4[i]):
                            c.append(i)
                else:
                    if(len(a[i])==2):    
                        b='00'+a[i]
                        for i in range(len(table_4)):
                            if (b==table_4[i]):
                                c.append(i)
                    else:
                        b='000'+a[i]
                        for i in range(len(table_4)):
                            if (b==table_4[i]):
                                c.append(i)
        for i in range(len(c)):
            match c[i]:
                case 10:
                    temp.append('A')
                case 11:
                    temp.append('B')
                case 12:
                    temp.append('C')
                case 13:
                    temp.append('D')
                case 14:
                    temp.append('E')
                case 15:
                    temp.append('F')
                case _:
                    for b in range(len(table_4)):
                        if (c[i]==b):
                            temp.append(b)
        temp.reverse()   
temp.reverse()
for i in temp:
    print(i,end="")