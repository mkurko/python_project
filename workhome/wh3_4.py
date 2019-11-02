print ("Program do przeliczania liczby zapisanej w formacie binarnym na dziesiętny")

iv_input = input("Podaj zapis binarny liczby: ")
test_list = ["1", "0"]
for i in iv_input:
    if i in test_list:
        pass
    else:
        print ("ups")
        exit (1)

print("Podano poprawnie liczbę binarnie: " + iv_input)
print("Liczba ta zamieniona na dziesiętny to: " + str(int(iv_input, 2)))

