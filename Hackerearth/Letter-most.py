def LetterMost(word):
    max=-1
    l1=[0]*255
    for i in word:
        l1[ord(i)]+=1
    for i in word:
        if max<l1[ord(i)]:
            max=l1[ord(i)]
    return max
length=int(input())
word=input()
print(LetterMost(word))