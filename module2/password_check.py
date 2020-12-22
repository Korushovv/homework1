password = input('Введите пароль: ')

try:
    password_len = len(password)
    check1 = 1/int(password_len)
    password_value = int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены')