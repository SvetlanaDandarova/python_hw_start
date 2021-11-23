num = int(input("Введите целое положительное число - "))
maximum = num % 10
num1 = num
while num1 > 0:
    digit = num1 % 10
    if digit > maximum:
        maximum = digit
    if digit == 9:
          break
    num1 //= 10
    print(num1)

print(f" Наибольшая цифра в числе {num} равна  {maximum}")
