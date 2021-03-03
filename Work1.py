count = int(input("Введите любое число: "))
pogran = int(input("Введите пограничное число: "))

if count < pogran:
    print("Введенное число меньше 10")
elif count > pogran:
    print("Введенное число больше 10")
elif count / pogran > 3:
    print("Введенное число больше 10 более чем в 3 раза")