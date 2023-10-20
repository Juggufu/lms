pas_1 = input()
pas_2 = input()
if len(pas_1) >= 8:
    if pas_1 == pas_2:
        print("OK")
    else:
        print("Различаются")
else:
    print("Короткий!")