l1=list(map(int,input("Enter first sorted array:").split()))
l2=list(map(int,input("Enter second sorted array:").split()))
l3=l1+l2
l3.sort()
l4=" ".join(map(str,l3))
print("Merged Sorted Array:",l4)