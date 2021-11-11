num = int(input("Enter a number: "))
print(f"number: {num}")
num1 = num
count = 0
while num1 > 1:
    num1 = num1/10
    count += 1
print(f"Count of digits: {count}")

j = 0
k = []
while j < count:
    k += 10**j,
    j += 1

i = 0
result = 0
while i < count:
    result += int(num/k[i]%10)
    i += 1
print(f"Addition of number digits: {result}")
