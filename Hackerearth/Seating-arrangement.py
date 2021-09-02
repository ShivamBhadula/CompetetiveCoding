for i in range(int(input())):
    seat=int(input())
    if seat%12==0:
        print(seat-11,'WS')
    elif seat%12==1:
        print(seat+11,'WS')
    elif seat%12==2:
        print(seat+9,'MS')
    elif seat%12==3:
        print(seat+7,'AS')
    elif seat%12==4:
        print(seat+5,'AS')
    elif seat%12==5:
        print(seat+3,'MS')
    elif seat%12==6:
        print(seat+1,'WS')
    elif seat%12==7:
        print(seat-1,'WS')
    elif seat%12==8:
        print(seat-3,'MS')
    elif seat%12==9:
        print(seat-5,'AS')
    elif seat%12==10:
        print(seat-7,'AS')
    elif seat%12==11:
        print(seat-9,'MS')