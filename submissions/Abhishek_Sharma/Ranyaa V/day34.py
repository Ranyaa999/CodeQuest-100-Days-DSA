queue = []

# Enqueue operation
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    value = int(input("Enter value: "))
    queue.append(value)  # enqueue

# Dequeue operation
d = int(input("Enter number of elements to dequeue: "))
for i in range(d):
    if queue:
        queue.pop(0)  # dequeue from front
    else:
        print("Queue is empty.")
        break

# Display remaining queue
print("Remaining Queue:", end=' ')
for item in queue:
    print(item, end=' ')
print()
