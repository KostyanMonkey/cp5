def to_8_or_2(base, number):
    under_zero = False
    if number < 0:
        under_zero = True
        number *= -1
    answer = ""
    while number > 0:
        answer = str(number % base) + answer
        number //= base
    if under_zero:
        return "-" + answer
    else:
        return answer
number = int(input("Введите число: "))
base = int(input("Введите целевую систему счисления: "))
while base != 2 and base !=8:
    print("Выберите двоичную или восьмиричную систему счисления")
    base = int(input("Введите целевую систему счисления: "))
answer = to_8_or_2(base, number)
print(number, "->", answer)