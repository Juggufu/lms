a = input()
con = 0
hmin = 999
hmax = 0
while a != "!":
    a = int(a)
    if 150 < a < 190:
        con += 1
        if a < hmin:
            hmin = a
        if a > hmax:
            hmax = a
    a = input()    
print(con)
print(hmin, hmax)


