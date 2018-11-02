print("K:")
K = int(input())

a = ((K % 7) + 3)%7
print(a)
if(a == 0):
    print("Sunday")
    
if(a == 1):
    print("Monday")

if(a == 2):
    print("Tuesday")

if(a == 3):
    print("Wednesday")

if(a == 4):
    print("Thursday")

if(a == 5):
    print("Friday")

if(a == 6):
    print("Saturday")


