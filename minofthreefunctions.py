# Read an integer:
a = int(input())
# Read a float:
b = int(input())
c = int(input())
min = a
# Print a value:
# print(a, b)
if(min > b):
    min = b
if(min > c):
    min = c
if(min > a):
    min = a
    
print(min)
