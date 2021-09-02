lst=[1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464, 171288, 195841, 216027, 216125, 262656, 314496, 320264, 327763, 373464, 402597, 443889, 515375, 525824, 558441, 593047, 684019]
t=int(input())
while t:
    t-=1
    mn=0
    a=int(input())
    if a<min(lst):
        print(-1)
    elif a>max(lst):
        print(max(lst))
    else:
        for i in range(0,len(lst)):
            if lst[i]<a and lst[i+1]>a:
                mn=lst[i]
        print(mn)