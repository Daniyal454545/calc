num = int(input('Введите первое число -> '))
oper = input("Введите только значении: '+'  '-'  '*' '/' '%' ")
num2 = int(input('Введите второе число (%) -> '))

if oper == '+':
    print(num + num2)
elif oper == '-':
    print(num - num2)
elif oper == '*':
    print(num * num2)
elif oper == '/':
    print(num / num2)
elif oper == '%':
    print((num * num2) / 100)
else:
    print("Данной операции нет в системе")



# простой но и не большой код, чем легче тем проще)