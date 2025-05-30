stack = []

# Push operation
n = int(input("Enter number of elements to push: "))
for _ in range(n):
    value = int(input("Enter value to push: "))
    stack.append(value)

# Pop operation
p = int(input("Enter number of elements to pop: "))
for _ in range(p):
    if stack:
        popped = stack.pop()
        print(f"Popped: {popped}")
    else:
        print("Stack is empty")
        break

# Display remaining stack
print("Current Stack:", end=' ')
for item in stack:
    print(item, end=' ')
print()
