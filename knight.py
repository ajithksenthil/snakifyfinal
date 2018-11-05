# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == 1 and abs(b - d) == 2 or abs(a - c) == 2 and abs(b - d) == 1 :
    print("YES")

else:
    print("NO")