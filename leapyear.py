# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())

if (a%4 == 0 and a % 100 != 0) or a % 400 == 0 :
    print("LEAP")

else:
    print("COMMON")