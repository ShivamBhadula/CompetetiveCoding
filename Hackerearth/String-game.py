test_case=int(input())
for i in range(test_case):
    string=input()
    a=list(string)
    a=list(dict.fromkeys(a))
    length=len(a)
    if length%2==0:
        print("Player2")
    else:
        print("Player1")