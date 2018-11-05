# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())
if c < a * b and ((c%b == 0) or (c%a == 0)) :
    print("YES")

else:
    print("NO")