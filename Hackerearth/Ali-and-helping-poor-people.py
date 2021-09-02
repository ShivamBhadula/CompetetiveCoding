code = input()
tag = code[2]
ta = 0
if tag != 'A' and tag != 'E' and tag != 'I' and tag != 'O' and tag != 'U' and tag != 'Y':
    for i in range(8):
 
        if (i ==0 or i==3 or i==4 or i==7):
            x = int(code[i])
            y = int(code[i + 1])
            if (x + y) % 2 == 0 and x!= 0:
                ta+=1
            else:
                print('invalid ')
                break
 
else:
    print('invalid')
if ta == 4:
    print('valid')