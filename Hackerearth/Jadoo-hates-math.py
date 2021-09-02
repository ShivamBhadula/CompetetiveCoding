number=int(input())
for i in range(number+1,number+14):
    if i%3!=0 and i%10!=3 and (i<30 or i>39):
        print(i)
        break