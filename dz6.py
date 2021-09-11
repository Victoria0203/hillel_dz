1.def reverse(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num //= 10
  return rev




2.lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

decimal = int(input("Enter a number: "))
hexadecimal = ''

while (decimal > 0):
    remainder = decimal % 16
    hexadecimal = lst[remainder] + hexadecimal
    decimal = decimal // 16

print("Hexadecimal: ", hexadecimal)




3.b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
   digit = b_num.pop()
   if digit == '1':
      value = value + pow(2, i)
print("The decimal value of the number is", value)



4.def HexToDec(h):
   return int(h, 16)

print("Enter Hexadecimal Number: ", end="")
hnum = input()

dnum = HexToDec(hnum)
print("\nEquivalent Decimal Value =", dnum)


5.m = number[0]
res = m
i = 1

while i < len(number):
   if number[i] < m:
      m = number[i]
      res -= number[i]
      i += 1

   else:
      m = number[i]
      res -= number[i]
      i += 1


print(f"Enter number: {res}")