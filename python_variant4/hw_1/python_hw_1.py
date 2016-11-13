a = float(input ('Введите а: '))
b = float(input ('Введите b: '))
c = float(input ('Введите c: '))
if ( a + b == c ):
    print('a и b в сумме дают c')
else:
    print('a и  b в сумме не дают с')
if b==0:
    print('недопустимое значение b: деление на 0')
else:
    if a/b==c:
        print('a разделить на b равно c')
    else:
        print('a разделить на b не равно c')
