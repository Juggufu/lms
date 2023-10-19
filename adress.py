login = input()
adress = input()
if "@" in login and not "@" in adress:
    print("Некорректный логин")
elif not "@" in adress and not "@" in login:
    print("Некорректный адрес")
else:
    print("OK")