dis=int(input())
online=list(map(int,input().split()))
offline=list(map(int,input().split()))
online_fare=online[0]+(dis-online[1])*online[2]
offline_fare=offline[1]+(dis//offline[1])*offline[2]+dis*offline[3]
if online_fare<=offline_fare:
    print('Online Taxi')
else:
    print('Classic Taxi')
