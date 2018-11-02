print("give me a two digit number")
a = int(input())
b = (a / 10)%10
print(int((a%10) * 10 + b))