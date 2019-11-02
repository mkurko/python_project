ln_input = input("Podaj kwotę: ")
try:
    lf_input = float(ln_input)
except ValueError:
    print ("zła wartośc")
    exit (5)

ln_5 = 0
ln_2 = 0
ln_1 = 0
ln_0_5 = 0
ln_0_2 = 0
ln_low = 0
lf_mny = lf_input

ln_5 = round((lf_input - round(lf_input % 5, 2)) / 5)
lf_input = lf_input - 5 * ln_5
print("Moneta 5zl: " + str(ln_5))

ln_2 = round((lf_input - round(lf_input % 2, 2)) / 2)
lf_input = lf_input - 2 * ln_2
print("Moneta 2zl: " + str(ln_2))

ln_1 = round((lf_input - round(lf_input % 1, 2)) / 1)
lf_input = lf_input - 1 * ln_1
print("Moneta 1zl: " + str(ln_1))

ln_0_5 = round((lf_input - round(lf_input % 0.5, 2)) / 0.5)
lf_input = lf_input - 0.5 * ln_0_5
print("Moneta 5gr: " + str(ln_0_5))

ln_0_2 = round((lf_input - round(lf_input % 0.2, 2)) / 0.2)
lf_input = lf_input - 0.2 * ln_0_2
print("Moneta 2gr: " + str(ln_0_2))

ln_low = round((lf_input - round(lf_input % 0.1, 2)) / 0.1)
lf_input = lf_input - 0.1 * ln_low
print("Moneta 1gr: " + str(ln_low))


