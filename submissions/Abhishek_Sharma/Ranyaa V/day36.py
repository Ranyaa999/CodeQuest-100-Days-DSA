s=input("enter a sentence")
words=s.lower().split()
freq={}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for k,v in freq.items():
    print(f"{k}:{v}")