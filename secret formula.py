a = input().split()  # Read the characters into a list
mp = {}  # Create an empty dictionary

# Map each index to its corresponding character
for i in range(10):
    mp[i] = a[i]

n = int(input())  # Read the value of n
b = list(map(int, input().split()))  # Read the list of integers

# Print the characters corresponding to the indices in b
for i in range(n):
    print(mp[b[i]], end="")

print()  # Print a newline