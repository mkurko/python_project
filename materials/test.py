liczba = (str(543543))
print (liczba[1:3])


# Dlatego też z zaokrąglaniem trzeba uważać
print(round(0.05, 1))  # oczekujemy 0.1 i jest ok
print("{:.27f}".format(0.05))
print(round(0.15, 1))  # oczekujemy 0.2 i jesteśmy zaskoczeni
print("{:.27f}".format(0.15))
print(round(0.0499999999999999999, 1))  # oczekujemy 0.0, a tu co innego
print("{:.27f}".format(0.0499999999999999999))


# Wartość maksymalna?
# int, long, czy long long?

number = 2 ** 63 - 1