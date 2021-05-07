# Тут решаем все задачи
# http://www.itmathrepetitor.ru/s-zadachi-s-resheniyami-chisla-i-cikly-2/
# каждая задача должна оформлятся в виде функции которая что-то ВОЗВРАЩАЕТ (не просто принтит, а чтото возвращает)

# 1. Составьте программу, выводящую на экран квадраты чисел от 10 до 20 включительно.
# def ex1(a, b):
# 	c = []
# 	for a in range(a, b + 1):
# 		a = a * a
# 		c.append(a)
# 	return print(c)
# ex1(10, 20)

#2. Даны натуральные числа от 35 до 87. Вывести на консоль те из них, которые при делении на 7 дают остаток 1, 2 или 5.
# def ex2(a, b):
# 	c = []
# 	for a in range(a, b + 1):
# 		if a%7 == 1 or a%7 == 2 or a%7 == 5:
# 			c.append(a)
# 	return print(c)
# ex2(35, 87)

#3. Найдите сумму  1+2+3+…+n, где число n вводится пользователем с клавиатуры.
def ex3():
    x = int(input('Введите число: '))
    y = 0
    for x in range(x+1):
        # print(x)
        y += x
    return print(y)
# ex3()

#4. Найдите произведение цифр трехзначного числа.
def ex4(a):
    a = str(a)
    return print(int(a[0]) * int(a[1]) * int(a[2]))
# ex4(234)


#5. Найдите количество четных цифр данного натурального числа.

def ex5(a):
    a = str(a)
    y = len(a)
    z = 0
    for x in a:
        x = int(x)
        if x%2 == 0:
            z += 1
    return print(z)
# ex5(22256668)

#6. Найдите наибольшую цифру данного натурального числа.
# def ex6(a):
#     a = str(a)
#     y = len(a)
#     z = [0]
#     for x in a:
#         x = int(x)
#         if x >= z[0]:
#             z[0] = x
#     return print(z[0])
# ex6(45641234)

# def ex6(a):
#     a = str(a)
#     y = len(a)
#     z = 0
#     for x in a:
#         x = int(x)
#         if x >= z:
#             z = x
#     return print(z)
# ex6(45841284)

#7. Найдите все четырехзначные числа, сумма цифр каждого из которых равна 15.
def ex7():
    z = []
    for x in range(1000, 10000):
        x = str(x)
        # print(x)
        y = int(x[0])+int(x[1])+int(x[2])+int(x[3])
        if y == 15:
            z.append(int(x))
    return z
# print(ex7())

#8. Определите, является ли натуральное число простым.
def ex8(x):
    w = 0
    y = x
    for x in range(1, x+1):
        if y%x == 0:
            w += 1
    if w == 2:
        return 'True'
    else:
        return 'False'
# print(ex8(5))

#9. Найдите все делители данного натурального числа.
# Любое натуральное число, на которое делится (без остатка) данное натуральное число, называется делителем данного числа.
def ex9(x):
    w = []                 # для счёта делителей числа
    y = x
    for x in range(1, x+1):
        if y%x == 0:
            w.append(x)
    return w
# print(ex9(6))

#10. Даны a и N. Вычислите aN без использования логарифма и экспоненты.

def ex10(a, n):
    y = 1
    for n in range(n):
        y = y * a
    return y
# print(ex10(4,3))

#11. В последовательности целых чисел найдите минимальное число и количество его повторений.

def ex11(x):
    y = x[0]
    for x in x:
        # print(x)
        if x < y:
            y = x
    return y                                             # минимальное
print(ex11([4, 5, 6, 17, 3, 88, 155.14]))