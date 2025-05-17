n=list(map(int,input("Enter numbers:").split()))
k=int(input("Enter rotation value (K):" ))
k=k%len(n)
r=n[-k:]+n[:-k]
r1=" ".join(map(str,r))
print(f"Rotated Array:{r1}")