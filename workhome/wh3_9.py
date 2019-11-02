print("Programu do wyliczania wieku psa")

ln_dog_years = int(input("ile lat ma pies: "))


ln_dog_years = int(ln_dog_years)
ln_h = 0.0
ln_d = 1
while ln_d <= ln_dog_years:
    if ln_d in (1, 2):
        ln_h = ln_h + 10.5
    else:
        ln_h = ln_h + 4
    ln_d = ln_d + 1

print("Wiek psi: " + str(ln_dog_years) + " przeliczając na lata ludzkie: " + str(ln_h))
