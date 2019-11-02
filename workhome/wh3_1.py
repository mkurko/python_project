# Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyswietlajac wzór i kolejne obliczenia)

print("program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyswietlajac wzór i kolejne obliczenia")
print("1 - stopnie Celcjusza na stopnie Fahrenheita")
print("2 - stopnie Fahrenheita na stopnie Celcjusza")
user_inpiut = input("Twój wybór: \n")
print ("wybrałeś:"  + user_inpiut)


def give_f(x):
    print (print("32+([Podana wartość stopni w Celcjuszach] * 9/5) = " + str(x)))
    return round((x * 9 / 5) + 32, 10)

if user_inpiut=="1":
    user_inpiut = float(input("Ile stopni:"))
    degree = give_f(user_inpiut)
    print("WYNIK:" + str(user_inpiut) + " stopni Celcjusza = "+str(degree) + " stopni Fahrenheita")
elif user_inpiut=="2":
    user_inpiut = float(input("Ile stopni:"))
    degree = round((user_inpiut - 32) * 5 / 9, 10)
    print("([Podana wartość stopni w Fahranhaitach]-32)*9/5) = " + str(degree))
    print("WYNIK:" + " stopni Fahranhaita to: "+str(degree) + " stopni Celcjusza.")
else:
    print("Podaj poprawną wartość")
    exit(1)